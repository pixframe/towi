#Django Core
from django.test import TestCase
import unittest
from django.utils import timezone
from django.core.urlresolvers import reverse

#Towi Imports
from ..models import *


class UserType_Test(unittest.TestCase):

    def setUp(self):
        UserType.objects.get_or_create(
            pk=1,
            description='Analista Test'
        )

    def test_string_representation_description(self):
        entry = UserType(description='Analista Test')
        self.assertEqual(str(entry), entry.description)


class Center_Test(TestCase):
    def setUp(self):
        Center.objects.get_or_create(
            pk=1,
            name='Centro Test',
            picture=None
        )
    
    def test_string_representation_center(self):
        center = Center(name='Center Test')
        self.assertEqual(str(center), center.name)


class School_Test(TestCase):
    def setUp(self):
        School.objects.get_or_create(
            name='School Test',
            type='private',
            regular_special='special',
            mixed_differetiated='men',
            city='México'
        )
    
    def test_string_represetation_school(self):
        school = School(name='School Test')
        self.assertEqual(str(school), school.name)


class User_Test(TestCase):
    def setUp(self):
        User.objects.get_or_create(
            email='test@gamil.com',
            password='towi123.',
            first_name='UserTest',
            last_name='LastTest',
            school=None,
            country='México',
            state='Edo_Mex',
            genre='Masculino',
            relation='Test',
            picture=None,
            dob=None,
            fb_id=None,
            phone=None,
            speciality='especialista',
        )
    
    def test_get_full_name(self):
        user = User(first_name='User')
        self.assertEqual(str(user), user.get_full_name)
    
    def test_get_short_name(self):
        user = User(first_name='Usertest')
        self.assertEqual(str(user), user.get_short_name)

    def test_display_name(self):
        user = User(first_name='Usertest')
        self.assertEqual(str(user), user.display_name)
    
    def test_key_string(slef):
        user = User(id=1, email='test@gmail.com')
        self.assertEqual(str(user), user.key_string)
    
    def test_get_inactive_childrens(self):
        self.assertEqual(User.get_inactive_childrens(), 1)
