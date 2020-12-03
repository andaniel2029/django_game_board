import datetime

from community.models import WarGame
from community.example_content.publishers import mini_war_games_publisher


infinity = WarGame(
    publisher=mini_war_games_publisher,
    name='Infinity',
    description='A dynamic and balanced skirmish game with the best metal miniatures on the market.',
    publication_date=datetime.datetime(2020, 10, 23),
    country='US',
)

age_of_sigmar = WarGame(
    publisher=mini_war_games_publisher,
    name='Age of Sigmar',
    description='A game that simulates battles between armies by using miniature figurines.',
    publication_date=datetime.datetime(2015, 1, 1),
    country='US',
)

malifaux = WarGame(
    publisher=mini_war_games_publisher,
    name='Malifaux',
    description='A game involving gang warfare in the ruins of a crumbling city.',
    publication_date=datetime.datetime(2009, 1, 1),
    country='US',
)
