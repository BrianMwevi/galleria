from django.test import TestCase
from account.models import Person
from django.contrib.auth.models import User

# Create your tests here.


class PersonTestCase(TestCase):
    # Setup method
    def setUp(self):
        self.user = User(username="johndoe",
                         email="johndoe@gmail.com", password="pass1123")
        self.user.save()
        self.person = Person(user=self.user, bio="Sample bio")

    def tearDown(self):
        User.objects.all().delete()
        Person.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.person, Person))

    def test_save_method(self):
        self.person.save_poster()
        persons = Person.objects.all()
        self.assertTrue(len(persons) == 1)
