from django.urls import path
from . import views

urlpatterns = [
    path('images', views.index, name='index'),
    path('vote/', views.vote_gif, name='vote_gif'),
]