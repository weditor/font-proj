from django.shortcuts import render
from rest_framework_mongoengine.viewsets import GenericViewSet, ModelViewSet

from .models import FontBlock, FontImage, ImageFile
from .serializers import FontBlockSerializer, FontImageSerializer

# from rest_framework.views import APIView

# Create your views here.


class FileView(GenericViewSet):
    model = ImageFile

    def create(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        pass


class FontImageView(ModelViewSet):
    model = FontImage
    serializer_class = FontImageSerializer
    filterset_fields = {"name": ["exact", "icontains"]}


class FontBlockView(ModelViewSet):
    model = FontBlock
    serializer_class = FontBlockSerializer
