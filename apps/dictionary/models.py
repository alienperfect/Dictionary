from django.db import models
from django.urls import reverse_lazy


class Word(models.Model):
    word = models.CharField(
        primary_key=True,
        max_length=256,
        unique=True,
        error_messages={'unique': 'This word already exists.'}
        )

    adjective = models.CharField(max_length=512, blank=True)
    adverb = models.CharField(max_length=512, blank=True)
    conjunction = models.CharField(max_length=512, blank=True)
    interjection = models.CharField(max_length=512, blank=True)
    noun = models.CharField(max_length=512, blank=True)
    preposition = models.CharField(max_length=512, blank=True)
    pronoun = models.CharField(max_length=512, blank=True)
    verb = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse_lazy('dictionary:word-detail', kwargs={'word': self.word})

    def get_parts_of_speech(self):
        PARTS_OF_SPEECH = (
            'adjective',
            'adverb',
            'conjunction',
            'interjection',
            'noun',
            'preposition',
            'pronoun',
            'verb'
            )

        parts = [part for part in PARTS_OF_SPEECH if getattr(self, part)]
        return parts
