# Generated by Django 4.0.2 on 2022-04-22 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=256)),
                ('pronunciation', models.FileField(upload_to='media/audio/')),
            ],
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.TextField()),
                ('word', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dictionary.word')),
            ],
        ),
        migrations.CreateModel(
            name='Pronoun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.TextField()),
                ('word', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dictionary.word')),
            ],
        ),
        migrations.CreateModel(
            name='Preposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.TextField()),
                ('word', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dictionary.word')),
            ],
        ),
        migrations.CreateModel(
            name='Noun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.TextField()),
                ('word', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dictionary.word')),
            ],
        ),
        migrations.CreateModel(
            name='Interjection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.TextField()),
                ('word', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dictionary.word')),
            ],
        ),
        migrations.CreateModel(
            name='Conjunction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.TextField()),
                ('word', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dictionary.word')),
            ],
        ),
        migrations.CreateModel(
            name='Adverb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.TextField()),
                ('word', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dictionary.word')),
            ],
        ),
        migrations.CreateModel(
            name='Adjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.TextField()),
                ('word', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dictionary.word')),
            ],
        ),
    ]