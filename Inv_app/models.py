from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    company = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name