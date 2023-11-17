from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Topico
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from datetime import date

@login_required(login_url = '/todolist/login/')
@require_http_methods(['GET', 'POST'])
def cadastro(request):
    if request.method == 'GET':
        params = {
            'active': True
        }
        return render(request, 'topico/cadastro.html', params)
    else:
        name = request.POST.get('name')
        deadline = request.POST.get('deadline')
        description = request.POST.get('description')
        
        topico = Topico(name = name, deadline = deadline, description = description, user_id = request.user.pk)
        topico.save()
        
        return redirect(reverse('site'))

@login_required(login_url = '/todolist/login/')
@require_http_methods(['GET'])
def all(request):
    pk = request.user.pk
    topicos = Topico.objects.filter(Q(user_id = pk) & Q(deadline__gte = date.today().__str__())).order_by('deadline')
    params = {
        'topicos': topicos,
        'active': True
    }
    return render(request, 'topico/topicos.html', params)

@login_required(login_url = '/todolist/login/')
@require_http_methods(['GET'])
def search(request):
    pk = request.user.pk
    keywords = request.GET.get('keywords')

    topicos = Topico.objects.filter(Q(user_id = pk) & Q(name__startswith = keywords))

    params = {
        'topicos': topicos,
        'active': True
    }

    return render(request, 'topico/search.html', params)

    
@login_required(login_url = '/todolist/login/')
@require_http_methods(['GET', 'POST'])
def edit(request, key):
    if request.method == 'GET':
        topico = Topico.objects.filter(pk = key).first()

        params = {
            'active': True,
            'topico': topico
        }

        return render(request, 'topico/edit.html', params)
    else:
        name = request.POST.get('name')
        deadline = request.POST.get('deadline')
        description = request.POST.get('description')

        Topico.objects.filter(pk = key).update(name = name, deadline = deadline, description = description)

        return redirect(reverse('topico.edit', args = [key]))
    
@login_required(login_url = '/todolist/login/')
@require_http_methods(['GET'])
def delete(request, key):
    Topico.objects.filter(pk = key).delete()
    return redirect(reverse('site'))