from community.models import CollectionItem

from community.example_content.enthusiasts import enthusiast_1, enthusiast_2, enthusiast_3
from community.example_content.board_games import pandemic, wingspan, space_base
from community.example_content.war_games import infinity, age_of_sigmar, malifaux
from community.example_content.card_games import magic_the_gathering, keyforge, pokemon
from community.example_content.role_playing_games import shadow_runner, mutant_chronicles, through_the_breach


collection_item_1 = CollectionItem(
    enthusiast=enthusiast_1,
    game=pandemic,
    has_played=True,
    currently_owns=True,
    previously_owned=True,
    would_sell=False,
    would_buy=False,
    would_trade=False
)

collection_item_2 = CollectionItem(
    enthusiast=enthusiast_3,
    game=wingspan,
    has_played=True,
    currently_owns=True,
    previously_owned=True,
    would_sell=True,
    would_buy=False,
    would_trade=False
)

collection_item_3 = CollectionItem(
    enthusiast=enthusiast_3,
    game=space_base,
    has_played=False,
    currently_owns=False,
    previously_owned=True,
    would_sell=False,
    would_buy=False,
    would_trade=False
)

collection_item_4 = CollectionItem(
    enthusiast=enthusiast_2,
    game=infinity,
    has_played=True,
    currently_owns=True,
    previously_owned=True,
    would_sell=False,
    would_buy=False,
    would_trade=False
)

collection_item_5 = CollectionItem(
    enthusiast=enthusiast_1,
    game=age_of_sigmar,
    has_played=True,
    currently_owns=True,
    previously_owned=True,
    would_sell=True,
    would_buy=False,
    would_trade=True
)

collection_item_6 = CollectionItem(
    enthusiast=enthusiast_1,
    game=malifaux,
    has_played=False,
    currently_owns=False,
    previously_owned=False,
    would_sell=False,
    would_buy=True,
    would_trade=False
)

collection_item_7 = CollectionItem(
    enthusiast=enthusiast_3,
    game=magic_the_gathering,
    has_played=False,
    currently_owns=False,
    previously_owned=True,
    would_sell=False,
    would_buy=False,
    would_trade=False
)

collection_item_8 = CollectionItem(
    enthusiast=enthusiast_2,
    game=keyforge,
    has_played=True,
    currently_owns=True,
    previously_owned=True,
    would_sell=False,
    would_buy=False,
    would_trade=False
)

collection_item_9 = CollectionItem(
    enthusiast=enthusiast_2,
    game=pokemon,
    has_played=True,
    currently_owns=False,
    previously_owned=True,
    would_sell=False,
    would_buy=False,
    would_trade=False
)

collection_item_10 = CollectionItem(
    enthusiast=enthusiast_1,
    game=shadow_runner,
    has_played=True,
    currently_owns=True,
    previously_owned=True,
    would_sell=True,
    would_buy=False,
    would_trade=True
)

collection_item_11 = CollectionItem(
    enthusiast=enthusiast_1,
    game=mutant_chronicles,
    has_played=True,
    currently_owns=True,
    previously_owned=True,
    would_sell=False,
    would_buy=False,
    would_trade=False
)

collection_item_12 = CollectionItem(
    enthusiast=enthusiast_3,
    game=through_the_breach,
    has_played=True,
    currently_owns=False,
    previously_owned=True,
    would_sell=False,
    would_buy=False,
    would_trade=False
)

