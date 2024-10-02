from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    seller = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    class CategoryChoices(models.TextChoices):
        TECHNOLOGY = 'TECH', 'Technology'
        CLOTHES = 'CLOTHES', 'Clothes'
        HOUSE_THINGS = 'HOUSE', 'House Things'
        MISC = 'MISC', 'Miscellaneous'

    category = models.CharField(
        max_length=10,
        choices=CategoryChoices.choices,
        default=CategoryChoices.MISC,
    )
    
    @property
    def is_good_rated(self):
        return self.rating >= 4