# Generated by Django 5.0.2 on 2024-03-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0005_alter_meal_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
