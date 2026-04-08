from django.db import models

# Create your models here.
class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='tecnologias/', blank=True)
    website = models.URLField(blank=True)
    classificacao = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='docentes/')
    pagina_pessoal = models.URLField(verbose_name="LinkedIn ou Site", blank=True)

    def __str__(self):
        return self.nome

class Area(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Contribuidor(models.Model):
    nome = models.CharField(max_length=200)
    pagina_pessoal = models.URLField(verbose_name="LinkedIn ou Site", blank=True)

    def __str__(self):
        return self.nome

class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel = models.IntegerField(help_text="Nível de 1 a 5")
    tecnologias = models.ManyToManyField(Tecnologia, related_name='competencias')

    def __str__(self):
        return self.nome


class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    num_semestres = models.IntegerField()
    formato = models.CharField(max_length=100)
    ects = models.IntegerField()
    competencias_adquiridas = models.TextField()

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    nome = models.CharField(max_length=200)
    codigo_uc = models.IntegerField(unique=True, null=True)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField()
    objetivos = models.TextField(blank=True)
    curricularIUnitReadableCode = models.TextField(blank=True)
    programa = models.TextField(blank=True)
    bibliografia = models.TextField(blank=True)
    metodologia = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True)
    docentes = models.ManyToManyField('Docente', related_name='ucs')

    def __str__(self):
        return f"{self.nome} ({self.licenciatura.nome})"

class Projeto(models.Model):
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos')
    titulo = models.CharField(max_length=200)
    conceitos = models.TextField()
    curso = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    github = models.URLField(blank=True)
    video = models.URLField(blank=True,null = True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    contribuidores = models.ManyToManyField(Contribuidor, related_name='projetos_colaborados')

    def __str__(self):
        return self.titulo

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    palavras_chave = models.CharField(max_length=200,blank=True,null=True)
    autor = models.CharField(max_length=200)
    curso = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='tfcs/')
    ano = models.IntegerField()
    resumo = models.TextField()
    relatorio = models.FileField(upload_to='tfcs/relatorios/')
    destaque = models.BooleanField(default=False)
    areas = models.ManyToManyField(Area, related_name='tfcs')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='tfcs')
    docentes_orientadores = models.ManyToManyField(Docente, related_name='tfcs_orientados')

    def __str__(self):
        return self.titulo


class Formacao(models.Model):
    titulo = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    ano_inicio = models.IntegerField()
    ano_fim = models.IntegerField(null=True, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='formacoes')

    def __str__(self):
        return self.titulo

class MakingOf(models.Model):
    data_registo = models.DateField(auto_now_add=True)
    fase = models.CharField(max_length=100)
    descricao_opcao = models.TextField()
    decisoes = models.TextField()
    erros_correcoes = models.TextField()
    uso_ai = models.TextField(verbose_name="Uso de IA")
    foto = models.ImageField(upload_to='making_of/',blank=True,null=True)

    def __str__(self):
        return f"Processo: {self.fase}"