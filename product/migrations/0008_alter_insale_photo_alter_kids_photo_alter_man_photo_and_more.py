# Generated by Django 5.0.1 on 2024-03-20 19:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "product",
            "0007_alter_insale_photo_alter_kids_photo_alter_man_photo_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="insale",
            name="photo",
            field=models.ImageField(upload_to="static/img/Insale_img"),
        ),
        migrations.AlterField(
            model_name="kids",
            name="photo",
            field=models.ImageField(upload_to="static/img/kids"),
        ),
        migrations.AlterField(
            model_name="man",
            name="photo",
            field=models.ImageField(upload_to="static/img/man_img"),
        ),
        migrations.AlterField(
            model_name="woman",
            name="photo",
            field=models.ImageField(upload_to="static/img/woman"),
        ),
    ]
