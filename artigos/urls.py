from django.urls import path

from . import views

app_name = "artigos"

urlpatterns = [
    path("", views.listagem, name="listagem"),
    path("novo/", views.criar_artigo, name="criar_artigo"),
    path("<int:artigo_id>/", views.detalhe, name="detalhe"),
    path("<int:artigo_id>/editar/", views.editar_artigo, name="editar_artigo"),
    path("<int:artigo_id>/like/", views.dar_like, name="like"),
    path("<int:artigo_id>/comentar/", views.adicionar_comentario, name="comentar"),
]
