from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('bali/', views.bali, name='bali'),
    path('blog/', views.blog, name='blog'),
    path('brahmatal/', views.brahmatal, name='brahmatal'),
    path('chopta/', views.chopta, name='chopta'),
    path('contact/', views.contact, name='contact'),
    path('dayara/', views.dayara, name='dayara'),
    path('flowers/', views.flowers, name='flowers'),
    path('hampta/', views.hampta, name='hampta'),
    path('harki/', views.harki, name='harki'),
    path('', views.index, name='index'),
    path('kauri/', views.kauri, name='kauri'),
    path('kedarkantha/', views.kedarkantha, name='kedarkantha'),
    path('phulara/', views.phulara, name='phulara'),
    path('policy/', views.policy, name='policy'),
    path('rupin/', views.rupin, name='rupin'),
    path('sar/', views.sar, name='sar'),
    path('trek/', views.trek, name='trek'),
]
