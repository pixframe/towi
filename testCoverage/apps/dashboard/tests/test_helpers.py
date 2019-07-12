import datetime
from django.test import TestCase

from suscriptions.models import Suscription, SuscriptionType
from accounts.models import User, Center


class TestCreateOrderId(TestCase):
    def test_create_order(self):
        center = Center.objects.create(
            name='TestCenter',
            picture=None
        )
        user = User.objects.create(
                email='test@gamil.com',
                password='towi123.',
                first_name='UserTest',
                last_name='LastTest',
                school=None,
                country='México',
                state='Edo_Mex',
                genre='Masculino',
                relation='Test',
                picture='/avatars/default_user.png',
                dob=None,
                fb_id='234874892749',
                phone=None,
                specialty='especialista',
                greeting='aajsdjalsda',
                center=center,
                confirmed_email=True,
                vcode='13jusdhf23uiufn',
                link_id='PXL34567',
                user_type='especialista',
                researcher=True,
                date_joined=datetime.datetime.now(),
                key='keyTest',
                openpay_token='23thdkfhuhnfjvbyahsd23',
                verified=True,
                is_active=True,
                is_staff=False,
                register_date=datetime.datetime.now(),
                account_type=1
        )
        suscription_type = SuscriptionType.objects.create(
            price=500,
            name='unsuscribe',
            description='test description'
        )
        suscription = Suscription.objects.get_or_create(
            user=user,
            type=suscription_type,
            children=children,
            start_date=datetime.datetime.now(),
            finished_date=datetime.datetime.now(),
            is_recurrent=True,
            trial=False,
            order='232389348'
        )
        self.create_order_id(suscription.id)
        self.assertTrue(suscription.create_order_id(suscription.id))
        self.assertEqual(suscription.order, '232389348')
