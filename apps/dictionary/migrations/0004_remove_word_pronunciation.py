# Generated by Django 4.0.2 on 2022-04-22 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_alter_word_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='pronunciation',
        ),
    ]
