# from django.urls import path, include
# from site_teste.views import sobre, contato

from django.urls import path, include
from site_teste.views import pag1, pag2, pag3
from . import views

# urlpatterns = [
#     path('', sobre),
#     path('contato/', views.index),
# ]

# from exemplo_site import views

urlpatterns = [
    path('', views.pag1, name='pag1'),
    path('pagina1/', views.pag1, name='pag1'),
    path('pagina2/', views.pag2, name='pag2'),
    path('pagina3/', views.pag3, name='pag3'),
]

