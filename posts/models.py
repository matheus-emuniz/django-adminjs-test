from django.db import models
from rest_framework import viewsets, serializers


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
