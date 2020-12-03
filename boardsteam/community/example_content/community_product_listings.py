from community.models import CommunityProductListing
from community.example_content.enthusiasts import enthusiast_1, enthusiast_2, enthusiast_3
from community.example_content.card_games import magic_the_gathering, keyforge, pokemon


community_list_1 = CommunityProductListing(
    enthusiast=enthusiast_1,
    game=magic_the_gathering,
    url="http:/mini_war_retailer/shadow_runner",
    price=50,
    description='Magic the Gathering'
)

community_list_2 = CommunityProductListing(
    enthusiast=enthusiast_2,
    game=keyforge,
    url="http:/mini_war_retailer/mutant_chronicles",
    price=20,
    description='Keyforge'
)

community_list_3 = CommunityProductListing(
    enthusiast=enthusiast_3,
    game=pokemon,
    url="http:/mini_war_retailer/through_the_breach",
    price=10,
    description='Through the Breach'
)
