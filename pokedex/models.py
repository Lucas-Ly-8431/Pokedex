from django.db import models

# Create your models here.

class Type(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Pokemon(models.Model):
    pokedex_number = models.PositiveIntegerField(primary_key = True)
    name = models.CharField(max_length=90)
    primarytype = models.ForeignKey(Type, null = True, on_delete = models.SET_NULL)
    secondarytype = models.ForeignKey(Type, null = True, on_delete = models.SET_NULL, related_name = "SecondaryType+")

    def __str__(self):
        return self.name
