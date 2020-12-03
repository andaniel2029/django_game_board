from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from polymorphic.models import PolymorphicModel
import os


def content_file_name(instance, filename):
    print(instance.collection_item.id)
    print(filename)
    return os.path.join('collection_images/' + str(instance.collection_item.id) + '/', filename)

class Enthusiast(AbstractUser):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='images')


class Business(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    logo = models.ImageField(upload_to='images')

    class Meta:
        abstract = True


class Publisher(Business):
    pass


class Retailer(Business):
    pass


class Language(models.Model):
    name = models.CharField(max_length=50)


class Game(PolymorphicModel):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    publication_date = models.DateField()
    country = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language)


class BoardGame(Game):
    pass


class WarGame(Game):
    pass


class CardGame(Game):
    pass


class RolePlayingGame(Game):
    pass


class CollectionItem(models.Model):
    enthusiast = models.ForeignKey(Enthusiast, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    has_played = models.BooleanField()
    currently_owns = models.BooleanField()
    previously_owned = models.BooleanField()
    would_sell = models.BooleanField()
    would_buy = models.BooleanField()
    would_trade = models.BooleanField()


class Card(models.Model):
    game = models.ForeignKey(CardGame, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')


class ProductListing(PolymorphicModel):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=500)


class RetailerProductListing(ProductListing):
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)


class CommunityProductListing(ProductListing):
    enthusiast = models.ForeignKey(Enthusiast, on_delete=models.CASCADE)


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    upload_date = models.DateTimeField()

    class Meta:
        abstract = True


class GameImage(Image):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class ProductListingImage(Image):
    listing = models.ForeignKey(ProductListing, on_delete=models.CASCADE)

#TODO: Check the below integration with Scott

class CollectionItemImage(models.Model):
    collection_item = models.ForeignKey(CollectionItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=content_file_name)