from django.db import models


class Word(models.Model):
    word = models.CharField(
        max_length=256,
        unique=True,
        error_messages={'unique': 'This word already exists.'}
        )

    adjective = models.TextField(blank=True)
    adverb = models.TextField(blank=True)
    conjunction = models.TextField(blank=True)
    interjection = models.TextField(blank=True)
    noun = models.TextField(blank=True)
    preposition = models.TextField(blank=True)
    pronoun = models.TextField(blank=True)
    verb = models.TextField(blank=True)

    def __str__(self):
        return self.word
