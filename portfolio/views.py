from django.shortcuts import render
from .models import Tecnologia,Docente,Formacao,Projeto,UnidadeCurricular,TFC,MakingOf
# Create your views here.
def home_view(request):
    return render(request, 'portfolio/base.html')

def tecnologias_list_view(request):
    context = {'tecnologias': Tecnologia.objects.all()}
    return render(request, 'portfolio/tecnologias.html', context)

def docentes_list_view(request):
    context = {'docentes': Docente.objects.all()}
    return render(request, 'portfolio/docentes.html', context)

def formacao_list_view(request):
    context = {'formacoes': Formacao.objects.all().prefetch_related('tecnologias')}
    return render(request, 'portfolio/formacao.html', context)

def projetos_list_view(request):
    context = {'projetos': Projeto.objects.all().prefetch_related('tecnologias', 'contribuidores')}
    return render(request, 'portfolio/projetos.html', context)

def ucs_list_view(request):
    context = {'ucs': UnidadeCurricular.objects.all().select_related('licenciatura')}
    return render(request, 'portfolio/disciplinas.html', context)

def tfcs_list_view(request):
    context = {'tfcs': TFC.objects.all().prefetch_related('docentes_orientadores', 'areas')}
    return render(request, 'portfolio/tfcs.html', context)

def making_of_list_view(request):
    context = {'registos': MakingOf.objects.all().order_by('-data_registo')}
    return render(request, 'portfolio/making_of.html', context)