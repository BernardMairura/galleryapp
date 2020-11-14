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

    def save_Location(self):
        self.save()

class Category(models.Model):
    name=models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_Category(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', null=True)
    name = models.CharField(max_length =60)
    description = models.TextField()
    Location = models.ForeignKey(Location, on_delete=models.CASCADE)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

    def save_Image(self):
        self.save()

    class Meta:
        ordering = ['Category']
     
