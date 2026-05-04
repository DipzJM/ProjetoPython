from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistoForm
from .models import MagicLinkToken
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


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

def send_magic_link(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            ml_token = MagicLinkToken.objects.create(user=user)
            
            link = request.build_absolute_uri(
                reverse('accounts:validar_magic_link', args=[str(ml_token.token)])
            )

            email_msg = EmailMessage(
                subject='O teu Link Magico',
                body=f'Clica aqui: {link}',
                from_email='noreply@portfolio.com',
                to=[email],
            )
            email_msg.send()
            
            return render(request, 'accounts/login.html', {'mensagem': 'Link enviado! verifica o terminal.'})
        except User.DoesNotExist:
            return render(request, 'accounts/login.html', {'mensagem': 'Email nao encontrado.'})

def validar_magic_link(request, token):
    try:
        ml_token = MagicLinkToken.objects.get(token=token)
        if ml_token.is_valid():
            ml_token.used = True
            ml_token.save()
            login(request, ml_token.user)
            return redirect('portfolio:base')
    except MagicLinkToken.DoesNotExist:
        pass
    return render(request, 'accounts/login.html', {'mensagem': 'Link inválido ou expirado.'})
