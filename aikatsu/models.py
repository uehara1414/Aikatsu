from django.db import models


class Verb(models.Model):
    word = models.CharField(max_length=16, primary_key=True)

    def __str__(self):
        return self.word
