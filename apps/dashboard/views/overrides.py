# DJANGO CORE IMPORTS
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

# TOWI IMPORTS
from reusable.tasks import send_email
from accounts.models import User


class CustomPasswordResetForm(PasswordResetForm):
    def send_mail(self, subject_template_name,
                  email_template_name, context,
                  from_email, to_email, html_email_template_name=None):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        user = context.pop('user', None)
        context['name'] = user.get_full_name
        context['email'] = to_email
        if 'uid' in context:
            uid = context['uid'].decode()
            context['uid'] = uid
        send_email.apply_async(('password', context))
        return reverse_lazy('password_reset_done')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email).exists():
            message = _("Este correo no esta registrado en Towi, por favor regístrate en Towi.")
            self.add_error('email', message)
        return email


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm