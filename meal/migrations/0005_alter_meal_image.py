# Generated by Django 5.0.2 on 2024-03-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0004_remove_meal_cuisine_type_remove_meal_dietary_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
