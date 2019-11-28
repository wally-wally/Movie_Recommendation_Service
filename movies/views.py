from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from .models import Genre, Movie, Comment
from .forms import CommentForm
from IPython import embed
from django.http import JsonResponse, HttpResponseBadRequest
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    if request.user.is_authenticated:
        recommend_movie = request.user.like_movies.all().last()
        genreinfo = recommend_movie.genre_id.first()
        recommend_info = []
        check_var = 0
        for movie in movies:
            genre_list = [genre for genre in movie.genre_id.all()]
            if genreinfo in genre_list:
                temp_dict = dict()
                temp_dict['pk'] = movie.pk
                temp_dict['poster_url'] = movie.poster_url
                temp_dict['name'] = movie.name
                temp_dict['director'] = movie.director
                recommend_info.append(temp_dict)
                check_var += 1
            if check_var == 3:
                break
        context = {'movies': movies, 'recommend_movie': recommend_movie, 'genreinfo': genreinfo, 'recommend_info': recommend_info,}
    else:
        context = {'movies': movies,}
    return render(request, 'movies/index.html', context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm()
    actors = movie.actor_set.all()
    context = {'movie': movie, 'comment_form': comment_form, 'comments': comments, 'actors': actors,}
    return render(request, 'movies/detail.html', context)

@require_POST
def comments_create(request, movie_pk):
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie_id = movie_pk
            comment.user = request.user
            comment.save()
            return redirect('movies:detail', movie_pk)
        else:
            return redirect('movies:index')
    return HttpResponse('No movie information', status=404)


@require_POST
def comments_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        return redirect ('movies:detail', movie_pk)
    return HttpResponse('No movie information', status=404)


@login_required
def like(request, movie_pk):
    if request.is_ajax():
        movie = get_object_or_404(Movie, pk=movie_pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            liked = False
        else:
            movie.like_users.add(request.user)
            liked = True
        context = {'liked': liked, 'count': movie.like_users.count(),}
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()