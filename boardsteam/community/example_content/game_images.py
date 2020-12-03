from django.utils import timezone

from community.models import GameImage
from community.example_content.board_games import pandemic, wingspan, space_base
from community.example_content.war_games import infinity, age_of_sigmar, malifaux
from community.example_content.card_games import magic_the_gathering, keyforge, pokemon
from community.example_content.role_playing_games import shadow_runner, mutant_chronicles, through_the_breach


pokemon_image = GameImage(
    game=pokemon,
    image='images/pokemon.jpg',
    upload_date=timezone.now(),
)

keyforge_image = GameImage(
    game=keyforge,
    image='images/keyforge.jpg',
    upload_date=timezone.now(),
)

magic_the_gathering_image = GameImage(
    game=magic_the_gathering,
    image='images/magic_the_gathering.jpg',
    upload_date=timezone.now(),
)

shadow_runner_image = GameImage(
    game=shadow_runner,
    image='images/shadow_runner.jpg',
    upload_date=timezone.now(),
)

mutant_chronicles_image = GameImage(
    game=mutant_chronicles,
    image='images/mutant_chronicles.jpg',
    upload_date=timezone.now(),
)

through_the_breach_image = GameImage(
    game=through_the_breach,
    image='images/through_the_breach.jpg',
    upload_date=timezone.now(),
)

infinity_image = GameImage(
    game=infinity,
    image='images/infinity.jpg',
    upload_date=timezone.now(),
)

age_of_sigmar_image = GameImage(
    game=age_of_sigmar,
    image='images/age_of_sigmar.jpg',
    upload_date=timezone.now(),
)

malifaux_image = GameImage(
    game=malifaux,
    image='images/malifaux.jpg',
    upload_date=timezone.now(),
)


pandemic_image = GameImage(
    game=pandemic,
    image='images/pandemic.jpg',
    upload_date=timezone.now(),
)

wingspan_image = GameImage(
    game=wingspan,
    image='images/wingspan.jpg',
    upload_date=timezone.now(),
)

space_base_image = GameImage(
    game=space_base,
    image='images/space_base.jpg',
    upload_date=timezone.now(),
)
