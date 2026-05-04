from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('registo/', views.registo, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('send_magic_link/', views.send_magic_link, name="send_magic_link"),
    path('validar_magic_link/<str:token>/', views.validar_magic_link, name="validar_magic_link"),
]