from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=256, unique=True)
    pronunciation = models.FileField(upload_to='media/audio/', blank=True, null=True)

    def __str__(self):
        return self.word


class Adjective(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)


class Adverb(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)


class Conjunction(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)


class Interjection(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)


class Noun(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)


class Preposition(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)


class Pronoun(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)


class Verb(models.Model):
    definition = models.TextField()
    word = models.OneToOneField('Word', on_delete=models.CASCADE)
