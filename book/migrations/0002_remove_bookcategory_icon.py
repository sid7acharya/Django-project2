# Generated by Django 5.0.5 on 2024-05-10 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcategory',
            name='icon',
        ),
    ]
