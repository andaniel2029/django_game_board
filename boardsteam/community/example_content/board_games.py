import datetime

from community.models import BoardGame
from community.example_content.publishers import board_games_publisher


pandemic = BoardGame(
    publisher=board_games_publisher,
    name='Pandemic',
    description='Pandemic is a cooperative board game designed by Matt Leacock and first published by Z-Man',
    publication_date=datetime.datetime(2008, 1, 1),
    country='UK',
)

wingspan = BoardGame(
    publisher=board_games_publisher,
    name='Wingspan',
    description='A medium-weight game in which players compete to attract birds to their wildlife reserves',
    publication_date=datetime.datetime(2019, 1, 4),
    country='US',
)

space_base = BoardGame(
    publisher=board_games_publisher,
    name='Space base',
    description='A quick-to-play dice game using the core "I roll, everyone gets stuff" mechanism seen in other games',
    publication_date=datetime.datetime(2020, 10, 23),
    country='US',
)
