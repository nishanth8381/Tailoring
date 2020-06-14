from django.urls import path
from .import views

urlpatterns= [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('list',views.List,name='list'),
    path('napkin',views.napkin,name='napkin'),
    path('pcover',views.pcover,name='pcover'),
    path('slip',views.slip,name='slip'),
    path('shimmi',views.shimmi,name='shimmi'),
    path('ufrock',views.ufrock,name='ufrock')
]