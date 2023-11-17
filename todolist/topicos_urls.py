
from django.urls import path
from . import topicos_views

urlpatterns = [
    path('cadastro/', topicos_views.cadastro, name = 'topico.cadastro'),
    path('all/', topicos_views.all, name = 'topico.all'),
    path('search/', topicos_views.search, name = 'topico.search'),
    path('edit/<int:key>/', topicos_views.edit, name = 'topico.edit'),
    path('delete/<int:key>/', topicos_views.delete, name = 'topico.delete')
]
