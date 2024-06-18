# Generated by Django 5.0.2 on 2024-06-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapi', '0002_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='author',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
