from typing import List, Optional

from .models import Game, Enthusiast


def get_most_relevant_games(game_class: Game, n_games: Optional[int] = 5) -> List[Game]:
    #TODO: use recommender system when it's implemented
    return game_class.objects.order_by('-publication_date')[:n_games]


def game_in_collection(enthusiast: Enthusiast, game: Game) -> bool:
    collection_items = enthusiast.collectionitem_set
    if collection_items.filter(game=game).count() == 0:
        return False
    else:
        return True
