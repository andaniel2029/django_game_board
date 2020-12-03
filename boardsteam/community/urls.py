from django.urls import path

from . import views

urlpatterns = [
    # ex: /community/
    path('', views.index, name='index'),
    # ex: /community/signup/
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # ex: /community/boardgames/X/  X is 1 to 3
    path('boardgames/<int:game_id>/', views.board_game_detail, name='board_game_detail'),
    # ex: /community/wargames/X/  X is 4 to 6
    path('wargames/<int:game_id>/', views.war_game_detail, name='war_game_detail'),
    # ex: /community/cardgames/X/  X is 7 to 9
    path('cardgames/<int:game_id>/', views.card_game_detail, name='card_game_detail'),    
    # ex: /community/cardgames/X/  X is 10 to 12
    path('rpggames/<int:game_id>/', views.rpg_game_detail, name='rpg_game_detail'),
    # ex: /community/enthusiasts/X/  X is 1 to 3
    path('enthusiasts/<int:enthusiast_id>/', views.enthusiast_profile, name='enthusiast_profile'),
    # ex: /community/enthusiasts/X/collection  X is 1 to 3
    path('enthusiasts/<int:enthusiast_id>/collection/uploads', views.enthusiast_collection_uploads, name='enthusiast_collection_uploads'),
    path('enthusiasts/<int:enthusiast_id>/collection/', views.enthusiast_collection, name='enthusiast_collection'),
    # ex: /community/enthusiasts/X/collection/Y/  X is 1 to 3
    path('enthusiasts/<int:enthusiast_id>/collection/<int:item_id>/', views.enthusiast_collection_item,
         name='enthusiast_collection_item'),
    # ex: /community/news/
    path('news/', views.news, name='news'),
    # ex: /community/forum/
    path('forum/', views.forum, name='forum'),
    # ex: /community/support/
    path('support/', views.support, name='support'),
    # ex: /community/addcollectionitem/X/
    path('addcollectionitem/<int:game_id>/', views.AddCollectionItemView.as_view(), name='add_collection_item'),
]
