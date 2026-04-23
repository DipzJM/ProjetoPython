from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='base'),
    path('tecnologias/', views.tecnologias_list_view, name='tecnologias'),
    path('docentes/', views.docentes_list_view, name='docentes'),
    path('formacao/', views.formacao_list_view, name='formacao'),
    path('projetos/', views.projetos_list_view, name='projetos'),
    path('ucs/', views.ucs_list_view, name='unidades_curriculares'),
    path('tfcs/', views.tfcs_list_view, name='tfcs'),
    path('making-of/', views.making_of_list_view, name='making_of'),
]