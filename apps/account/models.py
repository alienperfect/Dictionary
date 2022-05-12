from apps.dictionary.models import Word
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy


class Collection(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    words = models.ManyToManyField(Word)

    def get_absolute_url(self):
        return reverse_lazy('account:collection-detail', kwargs={'pk': self.pk})
