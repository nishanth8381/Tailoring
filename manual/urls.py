from django.urls import path
from .import views

urlpatterns= [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('list',views.List,name='list'),
    path('napkin',views.napkin,name='napkin')
]