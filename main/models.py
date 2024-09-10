from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    seller = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    
    @property
    def is_expensive(self):
        return self.price > 1000000