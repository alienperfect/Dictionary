# Generated by Django 4.0.2 on 2022-04-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0004_remove_word_pronunciation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adverb',
            name='word',
        ),
        migrations.RemoveField(
            model_name='conjunction',
            name='word',
        ),
        migrations.RemoveField(
            model_name='interjection',
            name='word',
        ),
        migrations.RemoveField(
            model_name='noun',
            name='word',
        ),
        migrations.RemoveField(
            model_name='preposition',
            name='word',
        ),
        migrations.RemoveField(
            model_name='pronoun',
            name='word',
        ),
        migrations.RemoveField(
            model_name='verb',
            name='word',
        ),
        migrations.AddField(
            model_name='word',
            name='adjective',
            field=models.TextField(blank=True, help_text='Definition'),
        ),
        migrations.AddField(
            model_name='word',
            name='adverb',
            field=models.TextField(blank=True, help_text='Definition'),
        ),
        migrations.AddField(
            model_name='word',
            name='conjunction',
            field=models.TextField(blank=True, help_text='Definition'),
        ),
        migrations.AddField(
            model_name='word',
            name='interjection',
            field=models.TextField(blank=True, help_text='Definition'),
        ),
        migrations.AddField(
            model_name='word',
            name='noun',
            field=models.TextField(blank=True, help_text='Definition'),
        ),
        migrations.AddField(
            model_name='word',
            name='preposition',
            field=models.TextField(blank=True, help_text='Definition'),
        ),
        migrations.AddField(
            model_name='word',
            name='pronoun',
            field=models.TextField(blank=True, help_text='Definition'),
        ),
        migrations.AddField(
            model_name='word',
            name='verb',
            field=models.TextField(blank=True, help_text='Definition'),
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(error_messages={'unique': 'This word already exists.'}, max_length=256, unique=True),
        ),
        migrations.DeleteModel(
            name='Adjective',
        ),
        migrations.DeleteModel(
            name='Adverb',
        ),
        migrations.DeleteModel(
            name='Conjunction',
        ),
        migrations.DeleteModel(
            name='Interjection',
        ),
        migrations.DeleteModel(
            name='Noun',
        ),
        migrations.DeleteModel(
            name='Preposition',
        ),
        migrations.DeleteModel(
            name='Pronoun',
        ),
        migrations.DeleteModel(
            name='Verb',
        ),
    ]
