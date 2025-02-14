# Generated by Django 5.0.2 on 2024-02-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='type',
            field=models.CharField(blank=True, choices=[('citrus', 'Citrus'), ('tropical', 'Tropical'), ('berries', 'Berries'), ('stone', 'Stone'), ('melons', 'Melons'), ('drupes', 'Drupes'), ('pome', 'Pome'), ('exotic', 'Exotic'), ('dried', 'Dried'), ('climacteric', 'Climacteric'), ('nonclimacteric', 'Nonclimacteric'), ('subtropical', 'Subtropical'), ('temperate', 'Temperate'), ('hardy', 'Hardy'), ('soft', 'Soft'), ('hard', 'Hard'), ('juicy', 'Juicy'), ('aromatic', 'Aromatic'), ('tart', 'Tart'), ('sweet', 'Sweet')], max_length=30, null=True),
        ),
    ]
