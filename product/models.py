from django.db import models
from django.core.urlresolvers import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
    description = models.CharField(max_length=1000)
    product_photo = models.FileField()

    def get_absolute_url(self):
        return reverse('product:product_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
