from django.db import models
# from django import forms
# Create your models here.


class NewsText(models.Model):
    text = models.CharField(blank=True, max_length=500)
