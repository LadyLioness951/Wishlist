from django.db import models

# Create your models here.
class Wishlist(models.Model):
    description = models.TextField(max_length=50)

    def __str__(self):
        return self.item
