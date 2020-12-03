from django.db.models import Model

from community.models import Language

from community.example_content.publishers import (mini_war_games_publisher, board_games_publisher,
    card_games_publisher, role_playing_games_publisher)

from community.example_content.retailers import (mini_war_games_retailer, board_games_retailer, card_games_retailer,
    role_playing_games_retailer)

from community.example_content.enthusiasts import enthusiast_1, enthusiast_2, enthusiast_3
from community.example_content.languages import english
from community.example_content.board_games import pandemic, wingspan, space_base
from community.example_content.war_games import infinity, age_of_sigmar, malifaux
from community.example_content.card_games import magic_the_gathering, keyforge, pokemon
from community.example_content.role_playing_games import shadow_runner, mutant_chronicles, through_the_breach

from community.example_content.retailer_product_listings import (war_games_retailer_list_1, war_games_retailer_list_2,
    war_games_retailer_list_3, board_games_retailer_list_1, board_games_retailer_list_2, board_games_retailer_list_3,
    role_playing_games_retailer_list_1, role_playing_games_retailer_list_2, role_playing_games_retailer_list_3,
    card_games_retailer_list_1, card_games_retailer_list_2, card_games_retailer_list_3)

from community.example_content.community_product_listings import community_list_1, community_list_2, community_list_3

from community.example_content.game_images import (pokemon_image, keyforge_image, magic_the_gathering_image,
    shadow_runner_image, mutant_chronicles_image, through_the_breach_image, infinity_image, age_of_sigmar_image,
    malifaux_image, pandemic_image, wingspan_image, space_base_image)

from community.example_content.cards import wildcard, bonus_card, penalty_card

from community.example_content.collection_items import (collection_item_1, collection_item_2, collection_item_3,
    collection_item_4, collection_item_5, collection_item_6, collection_item_7, collection_item_8, collection_item_9,
    collection_item_10, collection_item_11, collection_item_12)


def _add_language(model: Model, language: Language):
    model.languages.add(language)
    model.save()


# Publishers
mini_war_games_publisher.save()
board_games_publisher.save()
card_games_publisher.save()
role_playing_games_publisher.save()

# Retailers
mini_war_games_retailer.save()
board_games_retailer.save()
card_games_retailer.save()
role_playing_games_retailer.save()

# Enthusiasts
enthusiast_1.save()
enthusiast_2.save()
enthusiast_3.save()

# Languages
english.save()

# Board Games
pandemic.save()
_add_language(pandemic, english)

wingspan.save()
_add_language(wingspan, english)

space_base.save()
_add_language(space_base, english)

# War Games
infinity.save()
_add_language(infinity, english)

age_of_sigmar.save()
_add_language(age_of_sigmar, english)

malifaux.save()
_add_language(malifaux, english)

# Card Games
magic_the_gathering.save()
_add_language(magic_the_gathering, english)

keyforge.save()
_add_language(keyforge, english)

pokemon.save()
_add_language(pokemon, english)

# Role Playing Games
shadow_runner.save()
_add_language(shadow_runner, english)

mutant_chronicles.save()
_add_language(mutant_chronicles, english)

through_the_breach.save()
_add_language(through_the_breach, english)

# Retailer Product Listings
war_games_retailer_list_1.save()
war_games_retailer_list_2.save()
war_games_retailer_list_3.save()
board_games_retailer_list_1.save()
board_games_retailer_list_2.save()
board_games_retailer_list_3.save()
role_playing_games_retailer_list_1.save()
role_playing_games_retailer_list_2.save()
role_playing_games_retailer_list_3.save()
card_games_retailer_list_1.save()
card_games_retailer_list_2.save()
card_games_retailer_list_3.save()

# Community Product Listings
community_list_1.save()
community_list_2.save()
community_list_3.save()

# Game images
pokemon_image.save()
keyforge_image.save()
magic_the_gathering_image.save()
shadow_runner_image.save()
mutant_chronicles_image.save()
through_the_breach_image.save()
infinity_image.save()
age_of_sigmar_image.save()
malifaux_image.save()
pandemic_image.save()
wingspan_image.save()
space_base_image.save()

# Cards
wildcard.save()
bonus_card.save()
penalty_card.save()

# Collection Items
collection_item_1.save()
collection_item_2.save()
collection_item_3.save()
collection_item_4.save()
collection_item_5.save()
collection_item_6.save()
collection_item_7.save()
collection_item_8.save()
collection_item_9.save()
collection_item_10.save()
collection_item_11.save()
collection_item_12.save()
