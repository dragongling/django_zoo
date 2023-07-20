from django.urls import path

import base.animal_type_views
from . import views

urlpatterns = [
    path('animaltypes/', base.animal_type_views.animal_type_list_endpoint, name='animal types'),
    path('animaltypes/<int:pk>', base.animal_type_views.animal_type_detail_endpoint, name='animal type detail'),
    path('breeds/', views.breeds, name='breeds'),
    path('breeds/<int:pk>', views.breeds, name='breeds'),
    path('animals/', views.animals, name='animals'),
    path('animals/<int:pk>', views.animals, name='animals'),
    path('weightings/', views.weightings, name='weightings'),
    path('weightings/<int:pk>', views.weightings, name='weightings')
]
