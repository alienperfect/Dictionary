# Generated by Django 4.0.2 on 2022-04-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='pronunciation',
            field=models.FileField(blank=True, null=True, upload_to='media/audio/'),
        ),
    ]
