from django.db import models

# Create your models here.
class Offers(models.Model):
    Service=models.CharField(max_length=100 , default=' ')
    Percentag=models.CharField(max_length=100 , default=' ')
    Price=models.CharField(max_length=100 , default=' ')
    Image=models.ImageField(upload_to='pics', default=' ')
    def __str__(self):
        return self.Service
class Blogs(models.Model):
    title=models.CharField(max_length=100 , default=' ')
    image=models.ImageField(upload_to='pics', default=' ')
    text=models.TextField(max_length=100 , default=' ')
    def __str__(self):
        return self.title
class Serviceslider(models.Model):
    title=models.CharField(max_length=100 , default=' ')
    image=models.ImageField(upload_to='pics', default=' ')
    def __str__(self):
        return self.title
class Blogpage(models.Model):
    title=models.CharField(max_length=100 , default='')
    image=models.ImageField(upload_to='pics' , default='')
    date=models.DateTimeField(default='')
    description=models.TextField(max_length=200 , default='')
    def __str__(self):
        return self.title
