# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Iscritti(models.Model):
    class Meta:
        verbose_name="Iscritti"
        verbose_name_plural="Iscritti"

    # dati genari della persona
    nome=models.CharField(max_length=50, null=False)
    cognome=models.CharField(max_length=50, null=False)
    cf=models.CharField(max_length=16,null=False)
    data_nascita=models.DateField(null=True)

    # Dati del recapito della persona
    res_comune=models.CharField(max_length=50)
    res_recapito=models.CharField(max_length=150)


