from django.test import TestCase
from .models import Image,Location,Category,User


# Create your tests here.

class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.bernard= User(first_name = 'Bernard', last_name ='Mairura', email ='bernardmairura@gmail.com')


# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.bernard,User))




# Testing Save Method
    def test_save_method(self):
        self.bernard.save_User()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)



    # set up 
    def setUp(self):
        self.location = Location(location='mombasa')
        self.location.save()
        # categories
        self.category = Category(category='mombasa')
        self.category.save()

        # image
        self.image = Image(name='bernard', description='this is my name', location=self.location, category=self.category)
    # clean up after every test
    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    # est save in method
    def test_save(self):
        self.image
        self.image.image_save()
        self.assertTrue(len(Image.objects.all())>0)

    # test delete
    def test_delete(self):
        self.image
        self.image.image_save()
       
        
        self.image1.image_save()
        self.image1.image_delete()
        self.assertTrue(len(Image.objects.all()) == 1)