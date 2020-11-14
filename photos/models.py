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
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)

class Category(models.Model):
    name=models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_Category(self):
        self.save()


    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update()

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
    def search_image(cls,category):
        image = Image.objects.filter(category=Category)
        return image

    @classmethod
    def filter_by_location(cls,Location):
        image=Image.objects.filter(location=Location)
        return image


   

   

     
