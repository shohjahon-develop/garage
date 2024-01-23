from django.db import models

# Create your models here.

class Cars(models.Model):
   name=models.CharField(max_length=40)
   img=models.ImageField(upload_to='index/img')
   price=models.IntegerField()
   bio=models.TextField()

   def __str__(self):
       return self.name


class Lates(models.Model):
   nomi = models.CharField(max_length=100)
   price=models.IntegerField()
   bio=models.TextField()
   img = models.ImageField(upload_to='index/img')

   def __str__(self):
      return self.nomi









































