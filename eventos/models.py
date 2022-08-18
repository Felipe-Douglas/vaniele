from django.db import models

class Evento(models.Model):
    nome_evento = models.CharField(max_length=220)
    imagem_evento = models.CharField(max_length=200)
    data_evento = models.DateField()