import os
import sendgrid
import json
from datetime import date, timedelta, datetime
from django.core.mail import EmailMessage
from django.conf import settings
from accounts.api.serializers import UserSerializer
import calendar

class EmailSendgrid(object):

    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)

    def __init__(self, template, context, ts=None):
        self.template_id = self.get_template_id(template)
        self.context = context
        if template in ['compra_vencimiento', 'atencion', 'formas_uso']:
            data = {
                "personalizations": [
                    {
                        "to": [
                            {
                                "email": context['email']
                            }
                        ],
                        "send_at": self.get_unix(template),
                        "dynamic_template_data": self.context
                    }
                ],
                "from": {
                    "email": "hola@towi.com.mx"
                },
                "template_id": self.template_id
            }
        else:
            data = {
                "personalizations": [
                    {
                        "to": [
                            {
                                "email": context['email']
                            }
                        ],
                        "dynamic_template_data": self.context
                    }
                ],
                "from": {
                    "email": "hola@towi.com.mx"
                },
                "template_id": self.template_id
            }
        response = self.sg.client.mail.send.post(request_body=data)

    def get_template_id(self, template):
        if template == 'login':
            return 'd-df85ef1f8865449a852a3192a6f8e2dd'
        elif template == 'activation':
            return 'd-05a34579fe6a46968fd4afe030074faf'
        elif template == 'compra':
            return 'd-35b5b688f8634ab38ac3951e5f8461eb'
        elif template == 'password':
            return 'd-28ccab399344406c8a124cf7fb6ef003'
        elif template == 'prueba_finalizada':
            return 'd-90e1ed58359b4d039c42b460660f0212'
        elif template == 'seguimiento_creada':
            return 'd-85c94b24879c4fd29f57bd403c10869f'
        elif template == 'seguimiento_existente':
            return 'd-3f8fe462bf7a4b4890a3595e3ca150b1'
        elif template == 'compra_vencimiento':
            return 'd-a83a178477e5410087e8fc925c6ef2fe'
        elif template == 'atencion':
            return 'd-bb538e232a49452fb3113b60197dea8b'
        elif template == 'formas_uso':
            return 'd-439b9695e33c4107a755bce8b3fa403e'

    def get_unix(self, template):
        if template == 'atencion':
            time = datetime.utcnow() + timedelta(hours=48)
            unix = calendar.timegm(time.utctimetuple())
            return unix
        if template == 'formas_uso':
            time = datetime.utcnow() + timedelta(hours=70)
            unix = calendar.timegm(time.utctimetuple())
            return unix
