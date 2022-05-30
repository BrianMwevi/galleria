from django.test import TestCase
from django.contrib.auth.models import User
from account.models import Person
from galleria.models import Image, Category, Location

# Create your tests here.


class ImageTestCase(TestCase):
    # Setup method
    def setUp(self):
        self.user = User(username="johndoe",
                         email="johndoe@gmail.com", password="pass1123")
        self.user.save()
        self.poster = Person(user=self.user, bio="Sample bio")
        self.poster.save_poster()
        self.category = Category(name="Travel")
        self.category.save()
        self.location = Location(name="Nairobi")
        self.location.save()
        self.image = Image(photo="test.jpg", name="Image Name", description="Image description",
                           category=self.category, location=self.location, poster=self.user, )

    def tearDown(self):
        User.objects.all().delete()
        Person.objects.all().delete()
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_image_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image.save_image()
        self.image.name = "New Image Name"
        Image.update_image(self.image)
        updated_image = Image.objects.get(id=self.image.id)
        self.assertEqual(updated_image.name, 'New Image Name')

    def test_search_image_by_category(self):
        self.image.save_image()
        images = Image.search_image("Travel")
        self.assertTrue(len(images) == 1)

    def test_filter_image_by_location(self):
        self.image.save_image()
        images = Image.filter_by_location("Nairobi")
        self.assertTrue(len(images) == 1)


class TestCategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category(name="Travel")

    def tearDown(self):
        Category.objects.all().delete()

    def test_category_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 1)

    def test_update_category(self):
        self.category.save_category()
        self.category.name = "Nature"
        Category.update_category(self.category)
        updated_category = Category.objects.get(id=1)
        self.assertEqual(updated_category.name, "Nature")

    def test_delete_category(self):
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)
