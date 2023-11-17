from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Topico
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from datetime import date

# Create your views here.

@require_http_methods(['GET', 'POST'])
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'users/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user = User.objects.filter(username = username).first()

        if user:
            return HttpResponse('usuário já cadastrado') 

        user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, password = password, email = email)

        return redirect(reverse('login'))

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            login_django(request, user)

        return redirect(reverse('site'))

@login_required(login_url = '/todolist/login/')
@require_http_methods(['GET'])
def site(request):
    pk = request.user.pk
    topicos = Topico.objects.filter(user_id = pk).order_by('-start')[:5]

    params = {
        'topicos': topicos,
        'active': True
    }

    return render(request, 'site.html', params)

@login_required(login_url = '/todolist/login/')
@require_http_methods(['GET'])
def logout(request):
    logout_django(request)
    return redirect(reverse('login'))

@login_required(login_url = '/todolist/login/')
@require_http_methods(['GET'])
def profile(request):

    user = request.user
    pk = user.pk

    topicos = Topico.objects.filter(Q(user_id = pk) & Q(deadline__gte = date.today().__str__()))

    params = {
        'user': user,
        'active': True,
        'topicos': topicos
    }

    return render(request, 'users/profile.html', params)


@login_required(login_url = '/todolist/login/')
@require_http_methods(['GET', 'POST'])
def settings(request):
    if request.method == 'GET':
        user = request.user

        params = {
            'active': True,
            'user': user
        }

        return render(request, 'users/upd.html', params)
    else:
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        pk = request.user.pk

        User.objects.filter(pk = pk).update(first_name = first_name, last_name = last_name, email = email, password = password)

        return redirect(reverse('settings'))