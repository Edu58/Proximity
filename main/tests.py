import email
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Business, Neighbourhood, Profile, Post, Category

# class TestProfile(TestCase):

#     def setUp(self):
#         self.john = User(username="john",
#                          first_name="john",
#                          last_name="bravo",
#                          email="john@gmail.com",
#                          password="john98765")
#         self.john.save()

#         self.neighbourhood = Neighbourhood(name="sabina",
#                                            location="nrb",
#                                            number_of_occupants=3456,
#                                            health_dept_contact=75345345,
#                                            fire_dept_contact=74534534,
#                                            police_dept_contact=7435345,
#                                            admin=self.john)

#         self.neighbourhood.save()

#     def tearDown(self):
#         User.objects.all().delete()
#         Profile.objects.all().delete()
#         Neighbourhood.objects.all().delete()
#         Business.objects.all().delete()
#         Post.objects.all().delete()

#     def test_user_instance(self):
#         self.assertTrue(isinstance(self.john, User))

#     def test_profile_instance(self):
#         self.john_profile = Profile(
#             user=self.john,
#             neighbourhood = self.neighbourhood,
#             profile_pic="./media/profiles/17828.jpg",
#             bio="I am johny"
#         )

#         self.assertTrue(isinstance(self.john_profile, Profile))

# class TestNeighbourhood(TestCase):

#     def setUp(self):
#         self.john = User(username="john",
#                          first_name="john",
#                          last_name="bravo",
#                          email="john@gmail.com",
#                          password="john98765")
#         self.john.save()

#         self.neighbourhood = Neighbourhood(name="sabina",
#                                            location="nrb",
#                                            number_of_occupants=3456,
#                                            health_dept_contact=75345345,
#                                            fire_dept_contact=74534534,
#                                            police_dept_contact=7435345,
#                                            admin=self.john)

#         self.neighbourhood.save()

#     def tearDown(self):
#         User.objects.all().delete()
#         Profile.objects.all().delete()
#         Neighbourhood.objects.all().delete()
#         Business.objects.all().delete()
#         Post.objects.all().delete()

#     def test_neighbourhood_instance(self):
#         self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

#     def test_add_neighbourhood(self):
#         self.test_neighbourhood = Neighbourhood(name="cow",
#                                                 location="kakamega",
#                                                 number_of_occupants=34656,
#                                                 health_dept_contact=79345345,
#                                                 fire_dept_contact=74354534,
#                                                 police_dept_contact=74307345,
#                                                 admin=self.john)
#         self.test_neighbourhood.create_neighbourhood()

#         all_neighbourhoods = Neighbourhood.objects.all()
#         self.assertTrue(len(all_neighbourhoods) > 0)

#     def test_delete_neighbourhood(self):
#         self.neighbourhood.delete_neighbourhood()

#         all_neighbourhoods = Neighbourhood.objects.all()
#         self.assertTrue(len(all_neighbourhoods) == 0)


class TestBusiness(TestCase):

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

        self.business = Business(user=self.john,
                                 name="cookies",
                                 neighbourhood=self.neighbourhood,
                                 email='cookies@gmail.com',
                                 business_contact=723445345)

        self.business.save()

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Neighbourhood.objects.all().delete()
        Business.objects.all().delete()
        Post.objects.all().delete()

    def test_business_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_add_business(self):
        self.test_business = Business(user=self.john,
                                      name="shoes",
                                      neighbourhood=self.neighbourhood,
                                      email='shoes@gmail.com',
                                      business_contact=723845345)
        self.test_business.create_business()

        all_businesses = Business.objects.all()
        self.assertTrue(len(all_businesses) > 1)

    def test_delete_business(self):
        self.business.delete_business()

        all_businesses = Business.objects.all()
        self.assertTrue(len(all_businesses) == 0)