'''
Lembrar de registrar no arquivo admin.py
usando o 'from .models import [nome da classe]
e depois
'admin.site.register([nome da classe])
'''
from django.db import models
from django.conf import settings

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField()
    descicao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Transacoes'
    def __str__(self):
        return self.descricao

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
