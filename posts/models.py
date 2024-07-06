from django.db import models
from rest_framework import viewsets, serializers


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ('id', 'title', 'body')

class PostViewSet(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer