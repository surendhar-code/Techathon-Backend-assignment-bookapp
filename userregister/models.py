from django.db import models
from django.forms import ModelForm

# Create your models here.
class author(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return self.name

    

class genre(models.Model):
    genre=models.CharField(max_length=40)
    
    def __str__(self):
        return self.genre




class book(models.Model):
    bookname=models.CharField(max_length=100)
    author_name=models.ManyToManyField(author)
    price=models.FloatField()
    genre=models.ForeignKey(genre,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)

    