# Generated by Django 5.0.2 on 2024-02-16 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_sitevisit'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
