import json

from django.urls import reverse
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone

from rest_framework.test import APITestCase

from .factories import PruebaFactory, ChildrenFactory


class AssesmentAPITests(APITestCase):

    def setUp(self):
        self.prueba = PruebaFactory()
        self.header = self.prueba.header

    def test_create_succesfuly(self):
        data = {
            'header': {
                'date': self.header.date,
                'parent_id': self.header.parent.id,
                'kid_id':  self.header.cid.id,
                'game_key': self.header.gamekey,
                'game_time': self.header.gametime,
                'passed_levels': self.header.passedlevels,
                'repeated_levels': self.header.repeatedlevels,
                'played_levels': self.header.playedlevels
            },
            'levels': model_to_dict(self.prueba)
        }
        response = self.client.post(
            reverse("create-assesment"),
            {'jsonToDb': json.dumps(
                data,
                cls=DjangoJSONEncoder
            )},
        )
        self.assertEquals(response.status_code, 201)


class ChildrenLevelsAPITests(APITestCase):

    def setUp(self):
        self.children = ChildrenFactory()
        self.user = self.children.user

    def test_levels_children(self):
        data = {
            'userKey': self.user.key,
            'cid': self.children,
            'date': timezone.now().date()
        }
        response = self.client.post(
            reverse('children-levels-v2'),
            data,
        )
        self.assertEquals(response.status_code, 200)
