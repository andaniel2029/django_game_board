from community.models import Card
from community.example_content.card_games import magic_the_gathering, keyforge, pokemon


wildcard = Card(
    game=magic_the_gathering,
    name="wild card",
    description="allows activation of extra features",
    image="images/wild_card.jpg"
)

bonus_card = Card(
    game=keyforge,
    name="bonus card",
    description="bonus points during activation",
    image="images/bonus_card.jpg"
)

penalty_card = Card(
    game=pokemon,
    name="pokemon_card",
    description="activates penalty points",
    image="images/penalty_card.jpg"
)
