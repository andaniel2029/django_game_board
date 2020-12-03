import datetime

from community.models import CardGame
from community.example_content.publishers import card_games_publisher


magic_the_gathering = CardGame(
    publisher=card_games_publisher,
    name='Magic the Gathering',
    description='Each game represents a battle between wizards known as planeswalkers.',
    publication_date=datetime.datetime(2006, 1, 1),
    country='US',
)

keyforge = CardGame(
    publisher=card_games_publisher,
    name='Keyforge',
    description='A unique deck card game created by Richard Garfield and published by Fantasy Flight Games.',
    publication_date=datetime.datetime(2018, 1, 1),
    country='US',
)

pokemon = CardGame(
    publisher=card_games_publisher,
    name='Pokemon',
    description='Requires to raise a team of Pokémon to defeat other players.',
    publication_date=datetime.datetime(2005, 1, 1),
    country='Japan',
)
