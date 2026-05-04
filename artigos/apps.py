from django.apps import AppConfig


class ArtigosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "artigos"
    verbose_name = "Artigos"

    def ready(self):
        from django.db.models.signals import post_migrate
        from .signals import criar_grupo_autores_apos_migracao

        post_migrate.connect(criar_grupo_autores_apos_migracao)
