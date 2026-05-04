from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def criar_grupo_autores_apos_migracao(sender, app_config, **kwargs):
    if app_config.label != "artigos":
        return
    from .models import Artigo

    grupo, _ = Group.objects.get_or_create(name="autores")
    ct = ContentType.objects.get_for_model(Artigo)
    codenames = ("add_artigo", "change_artigo", "view_artigo")
    perms = Permission.objects.filter(content_type=ct, codename__in=codenames)
    grupo.permissions.set(perms)
