from django.contrib import admin
from .models import Artigo, Comentario, GostoArtigo


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "data_criacao")
    list_filter = ("data_criacao",)
    search_fields = ("titulo", "texto")
    readonly_fields = ("data_criacao", "autor")
    fieldsets = (
        (None, {"fields": ("titulo", "texto", "fotografia", "link_externo")}),
        ("Metadados", {"fields": ("autor", "data_criacao")}),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.groups.filter(name="autores").exists():
            return qs.filter(autor=request.user)
        return qs.none()

    def has_change_permission(self, request, obj=None):
        if not super().has_change_permission(request, obj):
            return False
        if obj is None:
            return True
        return request.user.is_superuser or obj.autor_id == request.user.id

    def has_add_permission(self, request):
        return super().has_add_permission(request) and (
            request.user.is_superuser
            or request.user.groups.filter(name="autores").exists()
        )

    def has_view_permission(self, request, obj=None):
        if obj is None:
            return super().has_view_permission(request, obj)
        if request.user.is_superuser:
            return super().has_view_permission(request, obj)
        return obj.autor_id == request.user.id and super().has_view_permission(
            request, obj
        )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("artigo", "autor", "data_criacao", "texto_preview")
    list_filter = ("data_criacao",)
    search_fields = ("texto", "artigo__titulo")

    @admin.display(description="Texto")
    def texto_preview(self, obj):
        t = (obj.texto or "")[:80]
        return t + ("…" if len(obj.texto or "") > 80 else "")


@admin.register(GostoArtigo)
class GostoArtigoAdmin(admin.ModelAdmin):
    list_display = ("artigo", "user", "session_key")
    list_filter = ("artigo",)
