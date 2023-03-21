from django.db import models
from tinymce import models as tinymce_models
class Property(models.Model):
    reference = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = tinymce_models.HTMLField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)