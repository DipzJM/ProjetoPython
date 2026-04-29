from django.shortcuts import render,redirect
from .models import Tecnologia,Docente,Formacao,Projeto,UnidadeCurricular,TFC,MakingOf,Competencia,Contribuidor
from .forms import ProjetoForm,FormacaoForm,TecnologiaForm,CompetenciaForm
from textwrap import dedent
# Create your views here.
def home_view(request):
    return render(request, 'portfolio/base.html')

def sobre_view(request):
    return render(request, 'portfolio/sobre.html')

def tecnologias_list_view(request):
    context = {'tecnologias': Tecnologia.objects.all().order_by('-id')}
    return render(request, 'portfolio/tecnologias.html', context)

def addTecnologias_list_view(request):
    form = TecnologiaForm(request.POST or None,request.FILES)
    if(form.is_valid()):
        form.save()
        return redirect('portfolio:tecnologias')

    context = {
        'form': form
    }
    return render(request, 'portfolio/addTecnologias.html',context)

def editarTecnologias_list_view(request,id):
    tecnologia = Tecnologia.objects.get(id=id)
    if request.POST:
        form = TecnologiaForm(request.POST or None, request.FILES, instance = tecnologia)
    
        if(form.is_valid()):
            form.save()
            return redirect('portfolio:tecnologias')
    else:
        form = TecnologiaForm(instance = tecnologia)
    context = {'form': form,'tecnologia':tecnologia}
    return render(request,'portfolio/editarTecnologias.html',context)

def apagarTecnologias_list_view(request ,id):
    tecnologia = Tecnologia.objects.get(id=id)

    tecnologia.delete()


    context = {'tecnologias': Tecnologia.objects.all()}
    return render(request,'portfolio/tecnologias.html',context)



def docentes_list_view(request):
    context = {'docentes': Docente.objects.all()}
    return render(request, 'portfolio/docentes.html', context)

def formacao_list_view(request):
    context = {'formacoes': Formacao.objects.all().prefetch_related('tecnologias')}
    return render(request, 'portfolio/formacao.html', context)

def addformacao_list_view(request):
    form = FormacaoForm(request.POST or None,request.FILES)
    if(form.is_valid()):
        form.save()
        return redirect('portfolio:formacao')

    context = {
        'form': form
    }
    return render(request, 'portfolio/addFormacao.html',context)

def editarformacao_list_view(request,id):
    formacao = Formacao.objects.get(id=id)
    if request.POST:
        form = FormacaoForm(request.POST or None, request.FILES, instance = formacao)
    
        if(form.is_valid()):
            form.save()
            return redirect('portfolio:formacao')
    else:
        form = FormacaoForm(instance = formacao)
    context = {'form': form,'formacao':formacao}
    return render(request,'portfolio/editarFormacao.html',context)

def apagarformacao_list_view(request ,id):
    formacao = Formacao.objects.get(id=id)

    formacao.delete()


    context = {'formacoes': Formacao.objects.all()}
    return render(request,'portfolio/formacao.html',context)


def competencias_list_view(request):
    context = {'competencias': Competencia.objects.all()}
    return render(request, 'portfolio/competencias.html', context)

def addCompetencias_list_view(request):
    form = CompetenciaForm(request.POST or None,request.FILES)
    if(form.is_valid()):
        form.save()
        return redirect('portfolio:competencias')

    context = {
        'form': form
    }
    return render(request, 'portfolio/addCompetencias.html',context)

def editarCompetencias_list_view(request,id):
    competencia = Competencia.objects.get(id=id)
    if request.POST:
        form = CompetenciaForm(request.POST or None, request.FILES, instance = competencia)
    
        if(form.is_valid()):
            form.save()
            return redirect('portfolio:competencias')
    else:
        form = CompetenciaForm(instance = competencia)
    context = {'form': form,'competencia':competencia}
    return render(request,'portfolio/editarCompetencias.html',context)

def apagarCompetencias_list_view(request ,id):
    competencia = Competencia.objects.get(id=id)

    competencia.delete()


    context = {'competencias': Competencia.objects.all()}
    return render(request,'portfolio/competencias.html',context)

def projetos_list_view(request):
    context = {'projetos': Projeto.objects.all().prefetch_related('tecnologias', 'contribuidores')}
    return render(request, 'portfolio/projetos.html', context)

def addprojeto_list_view(request):
    form = ProjetoForm(request.POST or None,request.FILES)
    if(form.is_valid()):
        form.save()
        return redirect('portfolio:projetos')

    context = {
        'ucs': UnidadeCurricular.objects.all(),
        'tecnologias':Tecnologia.objects.all(),
        'contribuidores':Contribuidor.objects.all(),
        'form': form
    }
    return render(request, 'portfolio/addprojeto.html',context)

def editarProjeto_list_view(request,id):
    projeto = Projeto.objects.get(id=id)
    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance = projeto)
    
        if(form.is_valid()):
            form.save()
            return redirect('portfolio:projetos')
    else:
        form = ProjetoForm(instance = projeto)
    context = {'form': form,'projeto':projeto}
    return render(request,'portfolio/editarProjeto.html',context)

def apagarProjeto_list_view(request ,id):
    projeto = Projeto.objects.get(id=id)

    projeto.delete()


    context = {'projetos': Projeto.objects.all().prefetch_related('tecnologias', 'contribuidores')}
    return render(request,'portfolio/projetos.html',context)






def ucs_list_view(request):
    context = {'ucs': UnidadeCurricular.objects.all().select_related('licenciatura')}
    return render(request, 'portfolio/disciplinas.html', context)

def tfcs_list_view(request):
    context = {'tfcs': TFC.objects.all().prefetch_related('docentes_orientadores', 'areas')}
    return render(request, 'portfolio/tfcs.html', context)

def making_of_list_view(request):
    context = {'registos': MakingOf.objects.all().order_by('-data_registo')}
    return render(request, 'portfolio/making_of.html', context)

from django.shortcuts import render
from textwrap import dedent

def makingApontamentos_of_list_view(request):
    # Utilizamos aspas triplas e dedent para manter a formatação do ficheiro .md
    texto = dedent("""
        # Diário de Bordo: Making Of - Portfólio Pessoal

        Este documento regista o processo de conceção, modelação e tomada de decisão para a aplicação de Portfólio Académico desenvolvida em Django.

        ---

        ## Registos do Trabalho em Papel
        *Os registos visuais de suporte a este documento (fotografias do caderno e esquemas) encontram-se na pasta `/media/makingof/` do repositório.*

        ### 1. Identificação de Entidades e Atributos Versão 1
        Após a análise detalhada do enunciado e a consulta de referências (DEISI/Lusófona), identifiquei as entidades para o sistema:
        * Licenciatura, Unidade Curricular (UC), Projetos, Tecnologias, TFCs, Formações, Competências e Making Of.
        * **Entidades Adicionais:** Docentes e Áreas.

        ---

        ## Modelação de Dados e Relações
        
        ### Versão 1
        * **Licenciatura (1:N) UC:** Uma licenciatura agrega várias disciplinas.
        * **UC (1:N) Projeto:** Projetos nascem no contexto de uma disciplina.
        * **Projeto (N:N) Tecnologia:** Relação de muitos-para-muitos entre ferramentas e trabalhos.
        * **Docente (N:N) UC:** Uma UC pode ter vários professores e vice-versa.

        ### Versão 2
        * **Projeto (1:N) Contribuidor:** Inclusão de equipas de desenvolvimento.

        ---

        ## ⚖️ Justificações das Decisões de Modelação

        ### 1. Licenciatura
        * **Decisão:** Inclusão do atributo `ECTS`.
        * **Justificação:** Decidi inserir os ECTS do Curso após análise do site da Lusófona.

        ### 3. Docentes (Entidade Adicional)
        * **Decisão:** Criação de entidade independente.
        * **Justificação:** Evita redundância (Normalização), permitindo atualizar dados de um docente em apenas um local.

        ### 5. Tecnologias
        * **Decisão:** Relação `ManyToMany` com Projetos e TFCs.
        * **Justificação:** Cria um sistema de filtros dinâmico no site.

        ### 11. Making Of
        * **Decisão:** Atributo `Uso AI`.
        * **Justificação:** Serve para documentar como as ferramentas de IA auxiliaram no desenvolvimento.

        ---

        ## Ajustes na modelação e decisões finais

        * **Decisão 3:** Criação da entidade 'Contribuidor' inspirada no modelo do LinkedIn para dar crédito a colaborações técnicas.
        * **Decisão 5:** Remoção da relação TFC -> Contribuidor após verificar que o ficheiro JSON original apenas continha o campo 'Autor'.
        * **Decisão 6:** Configuração do campo `palavras_chave` como nulo (`null=True`) para evitar erros na importação de dados do JSON.
    """).strip() # .strip() remove linhas em branco desnecessárias no início e fim

    context = {'texto': texto}
    return render(request, 'portfolio/making_ofApontamentos.html', context)