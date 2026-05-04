from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotografia = models.ImageField(upload_to="artigos/", blank=True, null=True)
    link_externo = models.URLField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="artigos",
    )

    class Meta:
        ordering = ["-data_criacao"]
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"

    def __str__(self):
        return self.titulo

    def total_likes(self):
        return self.gostos.count()


class GostoArtigo(models.Model):
    """Gosto de utilizador autenticado ou visitante (via sessão)."""

    artigo = models.ForeignKey(
        Artigo, on_delete=models.CASCADE, related_name="gostos"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="gostos_artigos",
    )
    session_key = models.CharField(max_length=40, blank=True, default="")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["artigo", "user"],
                condition=models.Q(user__isnull=False),
                name="gosto_artigo_por_utilizador",
            ),
            models.UniqueConstraint(
                fields=["artigo", "session_key"],
                condition=models.Q(user__isnull=True),
                name="gosto_artigo_por_sessao",
            ),
        ]

    def __str__(self):
        if self.user_id:
            return f"gosto {self.artigo_id} user {self.user_id}"
        return f"gosto {self.artigo_id} sessão"


class Comentario(models.Model):
    artigo = models.ForeignKey(
        Artigo, on_delete=models.CASCADE, related_name="comentarios"
    )
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comentarios_artigos"
    )
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["data_criacao"]

    def __str__(self):
        return f"Comentário de {self.autor} em {self.artigo}"
