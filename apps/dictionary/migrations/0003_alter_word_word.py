# Generated by Django 4.0.2 on 2022-04-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_alter_word_pronunciation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
