from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='base'),
    path('tecnologias/', views.tecnologias_list_view, name='tecnologias'),
    path('adicionarTecnologias/',views.addTecnologias_list_view, name='addTecnologias'),
    path('editarTecnologias/<int:id>',views.editarTecnologias_list_view, name='editarTecnologias'),
    path('apagarTecnologias/<int:id>/',views.apagarTecnologias_list_view, name='apagarTecnologias'),

    path('docentes/', views.docentes_list_view, name='docentes'),
    path('formacao/', views.formacao_list_view, name='formacao'),
    path('adicionarformacao/',views.addformacao_list_view, name='addformacao'),
    path('editarFormacao/<int:id>',views.editarformacao_list_view, name='editarFormacao'),
    path('apagarformacao/<int:id>/',views.apagarformacao_list_view, name='apagarFormacao'),


    path('projetos/', views.projetos_list_view, name='projetos'),
    path('adicionarProjetos/',views.addprojeto_list_view, name='addProjeto'),
    path('editarProjetos/<int:id>',views.editarProjeto_list_view, name='editarProjeto'),
    path('apagarProjeto/<int:id>/',views.apagarProjeto_list_view, name='apagarProjeto'),
    
    path('ucs/', views.ucs_list_view, name='unidades_curriculares'),
    path('competencias/', views.competencias_list_view, name='competencias'),
    path('adicionarCompetencias/',views.addCompetencias_list_view, name='addCompetencias'),
    path('editarCompetencias/<int:id>',views.editarCompetencias_list_view, name='editarCompetencias'),
    path('apagarCompetencias/<int:id>/',views.apagarCompetencias_list_view, name='apagarCompetencias'),

    path('tfcs/', views.tfcs_list_view, name='tfcs'),
    path('making-of/', views.making_of_list_view, name='making_of'),
]