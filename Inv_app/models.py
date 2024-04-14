from django.db import models

# Create your models here.
UNIT = [
    ('kg', 'Kilogramo'),
    ('gr', 'Gramo'),
    ('l', 'Litro'),
    ('ml', 'Mililitro'),
    ('un', 'Unidad'),
]

CATEGORY = [
    ('Lacteos', 'Lacteos'),
    ('Carnes', 'Carnes'),
    ('Huevos', 'Huevos'),
    ('Cereales', 'Cereales'),
    ('Frutas', 'Frutas'),
    ('Verduras', 'Verduras'),
    ('Dulces', 'Dulces'),
    ('Bebidas', 'Bebidas'),
]
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    company = models.CharField(max_length=20)
    category = models.CharField(max_length=10,choices=CATEGORY,default='Lacteos')
    unit = models.CharField(choices=UNIT,default='kg',max_length=10)
    price = models.FloatField(default=0)
    def __str__(self):
        return self.name