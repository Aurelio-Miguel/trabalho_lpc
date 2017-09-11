from django.db import models
from django.contrib.auth.models import User

'''class Endereco(models.Model):
    logradouro = models.CharField(max_length=128)
    complemento = models.CharField(max_length=256, null=True)
    uf = models.CharField(max_length=2, null=True)
    cidade = models.CharField(max_length=64, null=True)
    cep = models.CharField(max_length=10)

    def __str__(self):
        '{}, {}, {}'.format(self.logradouro, self.cidade, self.uf)'''

class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=100)
    '''descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name='pessoas', null=True, blank=False)
    usuario = models.OneToOneField(User)'''
    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=128)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=128)
    razaoSocial = models.CharField(max_length=128)

class Autor(Pessoa):
    curriculo = models.CharField(max_length=128)
    artigos = models.ArrayField (Artigo)

class Evento(models.Model):
    nome = models.CharField(max_length=128)
    eventoPrincipal = models.TextField(max_length=128)
    sigla = models.CharField(max_length=128)
    dataEHoraDeInicio = models.DateField(blank=True, null=True)
    palavrasChave = models.CharField(max_length=128)
    logotipo = models.CharField(max_length=128)
    realizador = models.ForeignKey(Pessoa, null = True, blank=False)
    cidade = models.CharField(max_length=128)
    uf = models.CharField(max_length=128)
    endereco = models.ForeignKey(Endereco, null=True, blank=False)
    numero = models.CharField(max_length=128)
    cep = models.CharField(max_length=128)   
    def __str__(self):
        return self.nome

class EventoCientifico(Evento):
    is sn = models.CharField(max_length=500)

class ArtigoCientifico():
    titulo = models.CharField(max_length=500)
    autores = models.ArrayField (Autor)
    evento = models.ForeignKey(EventoCientifico, null = True, blank=False)
    def __str__(self):
        return self.nome