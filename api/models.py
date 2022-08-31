
from django.db import models

# Create your models here.

class Task(models.Model):
    productn = models.CharField(max_length=50)  # Name of the brand
    category = models.CharField(max_length=50, default="") # category of clothing
    subcategory = models.CharField(max_length=50)   
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=30) # description of product
    pub_date = models.DateField() # date of delivery

    

    def __str__(self):
        return self.productn