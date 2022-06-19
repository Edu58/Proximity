from django.test import TestCase
from django.contrib.auth.models import User
from .models import Business, Neighbourhood, Profile, Post


class TestProfile(TestCase):

    def setUp(self):
        self.john = User(username="john",
                         first_name="john",
                         last_name="bravo",
                         email="john@gmail.com",
                         password="john98765")
        self.john.save()

        self.neighbourhood = Neighbourhood(name="sabina",
                                           location="nrb",
                                           number_of_occupants=3456,
                                           health_dept_contact=75345345,
                                           fire_dept_contact=74534534,
                                           police_dept_contact=7435345,
                                           admin=self.john)

        self.neighbourhood.save()

    def tearDown(self):
        self.john.delete()
        self.neighbourhood.delete()

    def test_user_instance(self):
        self.assertTrue(isinstance(self.john, User))

    def test_profile_instance(self):
        self.john_profile = Profile(
            user=self.john,
            neighbourhood = self.neighbourhood,
            profile_pic="./media/profiles/17828.jpg",
            bio="I am johny"
        )

        self.assertTrue(isinstance(self.john_profile, Profile))


