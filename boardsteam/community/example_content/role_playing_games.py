import datetime

from community.models import RolePlayingGame
from community.example_content.publishers import role_playing_games_publisher


shadow_runner = RolePlayingGame(
    publisher=role_playing_games_publisher,
    name='Shadow Runner',
    description='A speedrun-oriented platformer, where you can use classical mechanics like dashing or double jumping',
    publication_date=datetime.datetime(2019, 1, 1),
    country='US',
)

mutant_chronicles = RolePlayingGame(
    publisher=role_playing_games_publisher,
    name='Mutant Chronicles',
    description='A pen-and-paper role-playing game set in a post-apocalyptic world',
    publication_date=datetime.datetime(1993, 1, 1),
    country='Swedish',
)

through_the_breach = RolePlayingGame(
    publisher=role_playing_games_publisher,
    name='Through the Breach',
    description='A tabletop roleplaying game set in the world of Malifaux. ',
    publication_date=datetime.datetime(2018, 1, 1),
    country='US',
)
