from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    Name_Category = models.CharField(max_length=50)

class Langue(models.Model):
    Name_Langue = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    Category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    Langue = models.ForeignKey(Langue, null=True, blank=True, on_delete=models.CASCADE)
    emprunte = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    date_emprunt = models.DateField(null=True, blank=True)