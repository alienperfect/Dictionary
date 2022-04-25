from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.word


class Adjective(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)

    def __str__(self):
        return self._meta.model_name


class Adverb(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)

    def __str__(self):
        return self._meta.model_name


class Conjunction(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)

    def __str__(self):
        return self._meta.model_name


class Interjection(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)

    def __str__(self):
        return self._meta.model_name


class Noun(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)

    def __str__(self):
        return self._meta.model_name


class Preposition(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)

    def __str__(self):
        return self._meta.model_name


class Pronoun(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)

    def __str__(self):
        return self._meta.model_name


class Verb(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)

    def __str__(self):
        return self._meta.model_name
