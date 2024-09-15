from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    seller = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    
    @property
    def is_expensive(self):
        return self.price > 1000000