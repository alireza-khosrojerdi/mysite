# Generated by Django 4.2 on 2023-06-19 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_newsletter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Newsletter',
        ),
    ]