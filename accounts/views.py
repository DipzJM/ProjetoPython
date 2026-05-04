from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistoForm
from django.conf import settings

def registo(request):
    form = RegistoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('accounts:login')
    context = {'form': form}
    return render(request, 'accounts/registo.html', context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('portfolio:base')
        else:
            return render(request, 'accounts/login.html', {'form': form, 'mensagem': 'Credenciais inválidas'})
    
    return render(request, 'accounts/login.html', {'form': AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')