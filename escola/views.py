from django.shortcuts import render
from .models import Curso
# Create your views here.
def cursos_view(request):

    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    return render(request, 'escola/cursos.html', {'cursos': cursos})