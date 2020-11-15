from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=models.EmailField()

    def __str__(self):
        return self.first_name

    def save_User(self):
        self.save()



class Location(models.Model):
    location_name = models.CharField(max_length =30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)

class Category(models.Model):
    category_name=models.CharField(max_length=60)

    def __str__(self):
        return self.category_name

    def save_Category(self):
        self.save()


    def delete_category(self):
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(category_name=value)

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', null=True)
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['image']
    

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)

    @classmethod
    def get_image_by_id(cls,id):
        image = Image.objects.filter(id=Image.id)
        return image

    @classmethod
    def search_image(cls,category_name):
        image = Image.objects.filter(category_name=Category)
        return image

    @classmethod
    def filter_by_location(cls,Location):
        image=Image.objects.filter(location_name=Location)
        return image

    @classmethod
    def search_by_category(cls, search_term):
        image = cls.objects.filter(category__category_name__icontains=search_term)
        return image


   

   

     
