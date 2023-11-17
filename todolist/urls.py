from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('login/', views.login, name = 'login'),
    path('site/', views.site, name = 'site'),
    path('logout/', views.logout, name = 'logout'),
    path('topico/', include('todolist.topicos_urls')),
    path('profile', views.profile, name = 'profile'),
    path('settings', views.settings, name = 'settings')
]
