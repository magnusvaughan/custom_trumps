from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=200)


class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    physical_strength = models.IntegerField(default=0)
    fear_factor = models.IntegerField(default=0)
    killing_power = models.IntegerField(default=0)
    horror_rating = models.IntegerField(default=0)
