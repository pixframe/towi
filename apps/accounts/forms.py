# DJANGO CORE IMPORTS
from django import forms

# TOWI IMPORTS
from .models import User, Children, Center
from .choices import (
    LATERALITY_CHOICES,
    GENDER_CHOICES,
    GREETING_CHOICES,
    SCHOOLARSHIP_CHOICES
)


class EditAccountForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    specialty = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    genre = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    greeting = forms.ChoiceField(
        choices=GREETING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'style': 'display:none;'})
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'genre',
            'greeting', 'specialty',
            'picture'
        )


class InviteParentForm(forms.Form):
    USER_TYPES = (
        ('Padre', 'Padre'),
        ('Especialista', 'Especialista'),
        ('Escuela', 'Escuela'),
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control js-validate'})
    )
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    user_type = forms.ChoiceField(
        required=False,
        choices=USER_TYPES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        fields = (
            'email', 'password'
        )


class AddPatientForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    link_id = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        fields = (
            'email', 'password'
        )


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    child_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    child_dob = forms.DateField(
        required=False,
        input_formats=['%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y', '%d/%m/%Y'],
        widget=forms.HiddenInput()
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'email',
            'password',
            'password2',
        )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            self.add_error('password2', 'Las contraseñas no coinciden')


class RegisterLabForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    specialty = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    country = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'phone', 'specialty',
            'email', 'password', 'country'
        )


class ChildrenForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    dob = forms.DateField(
        required=True,
        input_formats=['%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y', '%d/%m/%Y'],
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'placeholder': "YYYY/MM/DD"}
        )
    )
    genre = forms.ChoiceField(
        required=False,
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    grade = forms.ChoiceField(
        required=False,
        choices=SCHOOLARSHIP_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'style': 'display:none;'})
    )
    diagnostic = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    laterality = forms.ChoiceField(
        required=False,
        choices=LATERALITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    failed_grades = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    videogames_usage = forms.FloatField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Numero de horas a la semana.'
            }
        )
    )

    class Meta:
        model = Children
        fields = (
            'first_name', 'last_name', 'dob',
            'picture', 'genre', 'laterality',
            'grade', 'diagnostic',
            'failed_grades', 'videogames_usage'
        )


class CenterForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'style': 'display:none;'})
    )

    class Meta:
        model = Center
        fields = (
            'name',
            'picture',
        )
