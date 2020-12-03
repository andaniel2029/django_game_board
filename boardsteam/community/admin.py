from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Enthusiast, Game, BoardGame, WarGame, CardGame, RolePlayingGame, RetailerProductListing, Card, \
    Language, GameImage, ProductListingImage, CollectionItemImage, CollectionItem


class LanguageInline(admin.TabularInline):
    model = Game.languages.through
    extra = 1


class CardInline(admin.TabularInline):
    model = Card
    extra = 3


class GameImageInline(admin.TabularInline):
    model = GameImage
    fields = ['image']
    extra = 3


class ProductListingImageInline(admin.TabularInline):
    model = ProductListingImage
    fields = ['image']
    extra = 3


class BoardGameAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'publisher', 'publication_date', 'country']
    inlines = [GameImageInline, LanguageInline]


class WarGameAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'publisher', 'publication_date', 'country']
    inlines = [GameImageInline, LanguageInline]


class CardGameAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'publisher', 'publication_date', 'country']
    inlines = [GameImageInline, CardInline, LanguageInline]


class RolePlayingGameAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'publisher', 'publication_date', 'country']
    inlines = [GameImageInline, LanguageInline]


class RetailerProductListingAdmin(admin.ModelAdmin):
    fields = ['game', 'description', 'price', 'url', 'retailer']
    inlines = [ProductListingImageInline]


admin.site.register(Enthusiast, UserAdmin)
admin.site.register(Language)
admin.site.register(BoardGame, BoardGameAdmin)
admin.site.register(WarGame, WarGameAdmin)
admin.site.register(CardGame, CardGameAdmin)
admin.site.register(RolePlayingGame, RolePlayingGameAdmin)
admin.site.register(RetailerProductListing, RetailerProductListingAdmin)
admin.site.register(CollectionItemImage)
admin.site.register(CollectionItem)

