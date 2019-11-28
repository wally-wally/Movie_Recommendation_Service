# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from IPython import embed
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {'users': users,}
    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        form = AuthenticationForm()
    context = {'form': form,}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def detail(request, user_pk):
    auth_user = get_object_or_404(get_user_model(), pk=user_pk)
    context = {'auth_user': auth_user,}
    return render(request, 'accounts/detail.html', context)

@login_required
def follow(request, user_pk):
    if request.is_ajax():
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                followed = False
            else:
                person.followers.add(user)
                followed = True
            context = {'followed': followed, 'count': person.followers.count(),}
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()

@login_required
def private(request, user_pk):
    user_profile = get_object_or_404(get_user_model(), pk=user_pk)
    context = {'user_profile': user_profile}
    return render(request, 'accounts/private.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
       form = PasswordChangeForm(request.user, request.POST)
       if form.is_valid():
           form.save()
           update_session_auth_hash(request, form.user)
           return redirect('accounts:private', request.user.id)
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form,}

    return render(request, 'accounts/authform2.html', context)

@require_POST
def delete(request):
    request.user.delete()
    return redirect('movies:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form,}
    return render(request, 'accounts/authform2.html', context)


def test(request):
    return render(request, 'accounts/test.html')