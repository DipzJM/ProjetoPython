from django.db import models

# Create your models here.
class licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.CharField(max_length=300)
    objetivos = models.CharField(max_length=200)
    competencias_adquiridas = models.CharField(max_length=200)
    formato = models.CharField(max_length=30)
    ects = models.IntegerField()
    nSemestres = models.IntegerField()

class unidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    imagem = models.UrlField()
    licenciatura = models.ForeignKey(licenciatura, on_delete=models.CASCADE,related_name='Licenciatura')