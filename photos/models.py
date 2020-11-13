from django.db import models

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=models.EmailField()

    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
