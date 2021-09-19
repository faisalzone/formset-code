from django.db import models

# Create your models here.


class Example(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    photo = models.ImageField(null=True, blank=True, upload_to='example')
