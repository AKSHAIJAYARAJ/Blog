from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('api/blog/',BlogManagerViewSet.as_view(),name='Blog'),
    path('api/like/',LikeManagerViewSet.as_view(),name='Like'),
    path('api/blog/details/',BlogLikesViewSet.as_view(),name='BlogLike'),
]