from django.db import models

class InSale(models.Model):
    photo = models.ImageField(upload_to='static/img/Insale_img', height_field=None, width_field=None, max_length=100)
    product_name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.product_name


class Man(models.Model):
    photo = models.ImageField(upload_to='static/img/man_img', height_field=None, width_field=None, max_length=100)
    product_name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.product_name

class Woman(models.Model):
    photo = models.ImageField(upload_to='static/img/woman', height_field=None, width_field=None, max_length=100)
    product_name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.product_name

class Kids(models.Model):
    photo = models.ImageField(upload_to='static/img/kids', height_field=None, width_field=None, max_length=100)
    product_name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.product_name

