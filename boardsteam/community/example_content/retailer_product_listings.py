from community.models import RetailerProductListing
from community.example_content.board_games import pandemic, wingspan, space_base
from community.example_content.war_games import infinity, age_of_sigmar, malifaux
from community.example_content.card_games import magic_the_gathering, keyforge, pokemon
from community.example_content.role_playing_games import shadow_runner, mutant_chronicles, through_the_breach
from community.example_content.retailers import (mini_war_games_retailer, board_games_retailer, card_games_retailer,
    role_playing_games_retailer)


war_games_retailer_list_1 = RetailerProductListing(
    retailer=mini_war_games_retailer,
    game=infinity,
    url="http:/mini_war_retailer/infinity_game",
    price=50,
    description='Infinity'
)

war_games_retailer_list_2 = RetailerProductListing(
    retailer=mini_war_games_retailer,
    game=age_of_sigmar,
    url="http:/mini_war_retailer/age_of_sigmar",
    price=20,
    description='Age of Sigmar'
)

war_games_retailer_list_3 = RetailerProductListing(
    retailer=mini_war_games_retailer,
    game=malifaux,
    url="http:/mini_war_retailer/malifaux",
    price=10,
    description='Malifaux'
)

board_games_retailer_list_1 = RetailerProductListing(
    retailer=board_games_retailer,
    game=pandemic,
    url="http:/mini_war_retailer/pandemic_game",
    price=50,
    description='Pandemic'
)

board_games_retailer_list_2 = RetailerProductListing(
    retailer=board_games_retailer,
    game=wingspan,
    url="http:/mini_war_retailer/wingspan",
    price=20,
    description='Wingspan'
)

board_games_retailer_list_3 = RetailerProductListing(
    retailer=board_games_retailer,
    game=space_base,
    url="http:/mini_war_retailer/space_base",
    price=10,
    description='Space Base'
)

role_playing_games_retailer_list_1 = RetailerProductListing(
    retailer=role_playing_games_retailer,
    game=shadow_runner,
    url="http:/mini_war_retailer/shadow_runner",
    price=50,
    description='Shadow Runner'
)

role_playing_games_retailer_list_2 = RetailerProductListing(
    retailer=role_playing_games_retailer,
    game=mutant_chronicles,
    url="http:/mini_war_retailer/mutant_chronicles",
    price=20,
    description='Mutant Chronicles'
)

role_playing_games_retailer_list_3 = RetailerProductListing(
    retailer=role_playing_games_retailer,
    game=through_the_breach,
    url="http:/mini_war_retailer/through_the_breach",
    price=10,
    description='Through the Breach'
)

card_games_retailer_list_1 = RetailerProductListing(
    retailer=card_games_retailer,
    game=magic_the_gathering,
    url="http:/mini_war_retailer/shadow_runner",
    price=50,
    description='Magic the Gathering'
)

card_games_retailer_list_2 = RetailerProductListing(
    retailer=card_games_retailer,
    game=keyforge,
    url="http:/mini_war_retailer/keyforge",
    price=20,
    description='Keyforge'
)

card_games_retailer_list_3 = RetailerProductListing(
    retailer=card_games_retailer,
    game=pokemon,
    url="http:/mini_war_retailer/pokemon",
    price=10,
    description='Pokemon'
)
