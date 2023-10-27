from django.urls import path

from .views import home, maison, boutique, terrain

urlpatterns = [
    path('home', home, name='home'),
    path('maison', maison, name='maison'),
    path('terrain', terrain, name='terrain'),
    path('boutique', boutique, name='boutique')

]
