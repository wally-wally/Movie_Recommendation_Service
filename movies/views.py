from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from .models import Genre, Movie, Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies,}
    return render(request, 'movies/index.html', context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm()
    context = {'movie': movie, 'comment_form': comment_form, 'comments': comments,}
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
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:detail', movie_pk)