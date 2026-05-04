from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ArtigoForm, ComentarioForm
from .models import Artigo, Comentario, GostoArtigo


def pertence_ao_grupo_autores(user):
    return user.is_authenticated and user.groups.filter(name="autores").exists()


def utilizador_gostou(artigo, request):
    if request.user.is_authenticated:
        return GostoArtigo.objects.filter(
            artigo=artigo, user=request.user
        ).exists()
    key = request.session.session_key
    if not key:
        return False
    return GostoArtigo.objects.filter(
        artigo=artigo, user__isnull=True, session_key=key
    ).exists()


def listagem(request):
    artigos = Artigo.objects.select_related("autor").all()
    return render(
        request,
        "artigos/listagem.html",
        {
            "artigos": artigos,
            "titulo_pagina": "Artigos",
            "e_autor": pertence_ao_grupo_autores(request.user),
        },
    )


def detalhe(request, artigo_id):
    artigo = get_object_or_404(
        Artigo.objects.select_related("autor").prefetch_related(
            "comentarios__autor"
        ),
        pk=artigo_id,
    )
    form = ComentarioForm()
    return render(
        request,
        "artigos/detalhe.html",
        {
            "artigo": artigo,
            "comentario_form": form,
            "titulo_pagina": artigo.titulo,
            "gostou": utilizador_gostou(artigo, request),
            "e_autor": pertence_ao_grupo_autores(request.user),
            "pode_editar": pertence_ao_grupo_autores(request.user)
            and artigo.autor_id == request.user.id,
        },
    )


@login_required
@user_passes_test(pertence_ao_grupo_autores)
def criar_artigo(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            messages.success(request, "Artigo publicado com sucesso.")
            return redirect("artigos:detalhe", artigo_id=artigo.pk)
    else:
        form = ArtigoForm()
    return render(
        request,
        "artigos/criar_artigo.html",
        {"form": form, "titulo_pagina": "Novo artigo"},
    )


@login_required
@user_passes_test(pertence_ao_grupo_autores)
def editar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    if artigo.autor_id != request.user.id:
        raise PermissionDenied

    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            messages.success(request, "Artigo atualizado.")
            return redirect("artigos:detalhe", artigo_id=artigo.pk)
    else:
        form = ArtigoForm(instance=artigo)

    return render(
        request,
        "artigos/editar_artigo.html",
        {
            "form": form,
            "artigo": artigo,
            "titulo_pagina": "Editar artigo",
        },
    )


@require_POST
def dar_like(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)

    if request.user.is_authenticated:
        gosto = GostoArtigo.objects.filter(artigo=artigo, user=request.user).first()
        if gosto:
            gosto.delete()
        else:
            GostoArtigo.objects.create(artigo=artigo, user=request.user, session_key="")
    else:
        if not request.session.session_key:
            request.session.create()
        key = request.session.session_key
        gosto = GostoArtigo.objects.filter(
            artigo=artigo, user__isnull=True, session_key=key
        ).first()
        if gosto:
            gosto.delete()
        else:
            GostoArtigo.objects.create(artigo=artigo, user=None, session_key=key)

    return redirect("artigos:detalhe", artigo_id=artigo.pk)


@login_required
@require_POST
def adicionar_comentario(request, artigo_id):
    artigo = get_object_or_404(
        Artigo.objects.select_related("autor").prefetch_related("comentarios__autor"),
        pk=artigo_id,
    )
    form = ComentarioForm(request.POST)
    if form.is_valid():
        c = form.save(commit=False)
        c.artigo = artigo
        c.autor = request.user
        c.save()
        messages.success(request, "Comentário adicionado.")
        return redirect("artigos:detalhe", artigo_id=artigo.pk)
    messages.error(request, "Não foi possível guardar o comentário.")
    return render(
        request,
        "artigos/detalhe.html",
        {
            "artigo": artigo,
            "comentario_form": form,
            "titulo_pagina": artigo.titulo,
            "gostou": utilizador_gostou(artigo, request),
            "e_autor": pertence_ao_grupo_autores(request.user),
            "pode_editar": pertence_ao_grupo_autores(request.user)
            and artigo.autor_id == request.user.id,
        },
    )
