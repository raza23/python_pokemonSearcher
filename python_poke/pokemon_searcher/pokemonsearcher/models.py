# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    fronturl = models.CharField(max_length=100)
    backurl = models.CharField(max_length=100)
    hp = models.IntegerField()

    def __str__(self):
        return self.name
