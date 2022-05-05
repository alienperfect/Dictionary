from django.db import models
from django.urls import reverse_lazy


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

    def get_absolute_url(self):
        return reverse_lazy('dictionary:word-detail', kwargs={'word': self.word})
