# Generated by Django 4.0.2 on 2022-05-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0006_alter_word_adjective_alter_word_adverb_and_more'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='words',
            field=models.ManyToManyField(to='dictionary.Word'),
        ),
    ]
