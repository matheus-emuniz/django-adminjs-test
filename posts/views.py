from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from posts.models import PostModel
from posts.serializers import PostSerializer

class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains', field_name='title')
    body = filters.CharFilter(lookup_expr='icontains', field_name='body')
    class Meta:
        model = PostModel
        fields = ['title', 'body']

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter

    @action(detail=False, methods=['GET'])
    def count(self, request):
        return Response({'count': PostModel.objects.count()})