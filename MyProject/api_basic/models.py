from django.db import models
from django.db.models.fields import DateTimeField



# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length = 100,default = '')
    email = models.EmailField(blank = True,max_length = 100)
    phone = models.CharField(blank = True,max_length = 20)
    comments = models.TextField(default = '')
    date = models.DateTimeField(auto_now_add = True) 

def __str__ (self):
    return self.name 