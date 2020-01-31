from django.contrib import admin

from .models import Deck, Card

class CardInline(admin.StackedInline):
    model = Card
    extra = 1


class DeckAdmin(admin.ModelAdmin):
    inlines = [CardInline]

admin.site.register(Deck, DeckAdmin)
admin.site.register(Card)