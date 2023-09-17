from django.urls import path
from .views import *

urlpatterns = [

    path('movies',MovieList.as_view()),
    path('actors',ActorList.as_view()),
    path('movies/<int:pk>',MovieDetail.as_view()),
    path('actors/<int:pk>',ActorDetail.as_view()),
    path('movies/<int:pk>/reviews',ReviewList.as_view()),
    
    
    
    
    
    
    # path('movies/<int:pk>/reviews',review_list),
    # path('movies', movie_list),
    # path('actors', actor_list),
    # path('movies/<int:pk>',movie_detail),
    # path('actors/<int:pk>',actor_detail),
]