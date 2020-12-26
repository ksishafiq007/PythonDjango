# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Myskill(models.Model):
    image=models.ImageField(upload_to='skillimage/')
    title=models.CharField(max_length=50,blank=False)
    desc=models.TextField(max_length=1000,blank=True)
    datetime=models.DateTimeField(auto_now_add=False)

    def summuary(self):
        return self.desc[0:150]

    def __str__(self):
        return self.title
    
