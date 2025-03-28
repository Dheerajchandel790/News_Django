from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoery(models.Model):
     title = models.CharField( max_length=50)
     img = models.ImageField( upload_to='cate/')
     
     def __str__(self):
         return self.title
     

class News(models.Model):
     user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True , blank=True) 
     Categoery = models.ForeignKey(Categoery,on_delete=models.CASCADE)
     title = models.CharField( max_length=50)
     description = models.TextField()
     img = models.ImageField( upload_to='News/')
     
     date = models.DateTimeField( auto_now_add=True)
     
     def __str__(self):
         return self.title
     
     class Meta:
          verbose_name_plural = 'News'

     