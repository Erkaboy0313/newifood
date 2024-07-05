# Generated by Django 5.0.2 on 2024-07-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0004_alter_fruit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='confirmed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='fruit',
            name='status',
            field=models.CharField(blank=True, choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=100),
        ),
    ]
