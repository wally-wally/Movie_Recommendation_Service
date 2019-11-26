from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/', views.detail, name='detail'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('private/<int:user_pk>/', views.private, name='private'),
    path('change_password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('test/', views.test, name='test'),
]
