import json

from django.db import models


# Create your models here.
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    age = models.IntegerField()

    def __cmp__(self, other):
        return hash(self.id) - hash(other.id)

    def __eq__(self, other):
        return (self.id == other.id)

    def __hash__(self):
        return hash(self.id)
