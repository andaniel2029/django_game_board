from typing import Union

from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import Game, BoardGame, WarGame, CardGame, RolePlayingGame, Enthusiast, CollectionItem, CollectionItemImage
from .forms import EnthusiastCreationForm, CollectionItemForm
from .utils import get_most_relevant_games, game_in_collection


class SignUpView(generic.CreateView):
    form_class = EnthusiastCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'board_games': get_most_relevant_games(BoardGame),
        'war_games': get_most_relevant_games(WarGame),
        'card_games': get_most_relevant_games(CardGame),
        'rpg_games': get_most_relevant_games(RolePlayingGame),
    }
    return render(request, 'community/index.html', context)


def board_game_detail(request: HttpRequest, game_id: int) -> Union[HttpResponse, Http404]:
    game = get_object_or_404(BoardGame, pk=game_id)
    context = {'game': game}
    if request.user.is_authenticated:
        context['in_collection'] = game_in_collection(request.user, game)
    return render(request, 'community/board_game_detail.html', context)


def war_game_detail(request: HttpRequest, game_id: int) -> Union[HttpResponse, Http404]:
    game = get_object_or_404(WarGame, pk=game_id)
    context = {'game': game}
    if request.user.is_authenticated:
        context['in_collection'] = game_in_collection(request.user, game)
    return render(request, 'community/war_game_detail.html', context)


def card_game_detail(request: HttpRequest, game_id: int) -> Union[HttpResponse, Http404]:
    game = get_object_or_404(CardGame, pk=game_id)
    context = {'game': game}
    if request.user.is_authenticated:
        context['in_collection'] = game_in_collection(request.user, game)
    return render(request, 'community/card_game_detail.html', context)


def rpg_game_detail(request: HttpRequest, game_id: int) -> Union[HttpResponse, Http404]:
    game = get_object_or_404(RolePlayingGame, pk=game_id)
    context = {'game': game}
    if request.user.is_authenticated:
        context['in_collection'] = game_in_collection(request.user, game)
    return render(request, 'community/rpg_game_detail.html', context)


def enthusiast_profile(request: HttpRequest, enthusiast_id: int) -> Union[HttpResponse, Http404]:
    enthusiast = get_object_or_404(Enthusiast, pk=enthusiast_id)
    context = {'enthusiast': enthusiast}
    return render(request, 'community/enthusiast_profile.html', context)


def enthusiast_collection(request: HttpRequest, enthusiast_id: int) -> Union[HttpResponse, Http404]:
    enthusiast = get_object_or_404(Enthusiast, pk=enthusiast_id)
    context = {'enthusiast': enthusiast}
    return render(request, 'community/enthusiast_collection.html', context)


@csrf_exempt
def enthusiast_collection_uploads(request, enthusiast_id):
    print('11111')
    if request.method == 'POST':

        collection_item_id = request.POST.get('collection_item')
        images = request.FILES.getlist('images')

        collection_item = get_object_or_404(CollectionItem, pk=collection_item_id)

        print(collection_item)
        print(images)


        # create new CollectionItemImage
        for img in images:
            print(img)
            collection_item_image = CollectionItemImage( collection_item=collection_item, image=img )
            collection_item_image.save()
            print('created!!!')

        data = {
            'status': 'success'
        }
        return JsonResponse(data)
    data = {
        'msg': 'Upload files'
    }
    return JsonResponse(data)


def enthusiast_collection_item(request: HttpRequest, enthusiast_id: int, item_id: int) -> Union[HttpResponse, Http404]:
    enthusiast = get_object_or_404(Enthusiast, pk=enthusiast_id)
    item = get_object_or_404(CollectionItem, pk=item_id)
    if request.method == 'POST':
        if request.POST.get('remove_item', False):
            item.delete()
            return HttpResponseRedirect(
                reverse_lazy('enthusiast_collection', kwargs={'enthusiast_id': enthusiast_id})
            )

    context = {
        'enthusiast': enthusiast,
        'item': item
    }
    return render(request, 'community/enthusiast_collection_item.html', context)


def news(request: HttpRequest) -> Union[HttpResponse, Http404]:
    context = {'foo': 'bar'}
    return render(request, 'community/news.html', context)


def support(request: HttpRequest) -> Union[HttpResponse, Http404]:
    context = {'foo': 'bar'}
    return render(request, 'community/support.html', context)


def forum(request: HttpRequest) -> Union[HttpResponse, Http404]:
    context = {'foo': 'bar'}
    return render(request, 'community/forum.html', context)


class AddCollectionItemView(generic.CreateView):
    form_class = CollectionItemForm
    template_name = 'community/add_collection_item.html'

    def get_success_url(self):
        return reverse_lazy('enthusiast_collection', kwargs={'enthusiast_id': self.request.user.id})

    def get_context_data(self, **kwargs):
        context = super(AddCollectionItemView, self).get_context_data(**kwargs)
        context['game'] = get_object_or_404(Game, pk=self.kwargs['game_id'])
        return context

    def form_valid(self, form):
        form.instance.enthusiast = self.request.user
        form.instance.game = get_object_or_404(Game, pk=self.kwargs['game_id'])
        return super(AddCollectionItemView, self).form_valid(form)
