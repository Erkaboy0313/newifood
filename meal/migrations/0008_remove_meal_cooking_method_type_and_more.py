# Generated by Django 5.0.2 on 2024-07-01 10:54

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0007_alter_country_options_alter_meal_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='cooking_method_type',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='meal_type',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='recipe',
        ),
        migrations.AlterField(
            model_name='meal',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]
