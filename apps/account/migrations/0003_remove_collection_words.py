# Generated by Django 4.0.2 on 2022-05-12 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_collection_words'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='words',
        ),
    ]
