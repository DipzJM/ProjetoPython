from django.contrib import admin
from .models import UnidadeCurricular
from .models import Projeto
from .models import TFC
from .models import Tecnologia
from .models import Docente
from .models import Competencia
from .models import Licenciatura
from .models import Area
from .models import Contribuidor
from .models import Formacao
from .models import MakingOf

# Register your models here.
@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'licenciatura', 'ano', 'semestre', 'ects')
    list_filter = ('licenciatura', 'ano', 'semestre')
    search_fields = ('nome',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'uc', 'autor')
    list_filter = ('uc__licenciatura', 'tecnologias')
    search_fields = ('titulo', 'descricao', 'conceitos')

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'destaque')
    list_filter = ('destaque', 'ano', 'areas')
    search_fields = ('titulo', 'resumo', 'palavras_chave')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'classificacao')
    search_fields = ('nome', 'classificacao')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel')
    list_filter = ('nivel',)


admin.site.register(Licenciatura)
admin.site.register(Area)
admin.site.register(Contribuidor)
admin.site.register(Formacao)
admin.site.register(MakingOf)