from django.db import models

class Sale(models.Model):
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    product_name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.product_name

class Man(models.Model):
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    product_name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.product_name

class Woman(models.Model):
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    product_name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.product_name


class Kids(models.Model):
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    product_name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.product_name