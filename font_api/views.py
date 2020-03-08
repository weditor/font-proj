from django.shortcuts import render
from rest_framework_mongoengine.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from django.http.response import FileResponse

from .models import FontBlock, FontImage, ImageFile, ImageStatus
from .serializers import FontBlockSerializer, FontImageSerializer
from datetime import datetime
from rest_framework.decorators import action

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
    queryset = FontImage.objects.all()
    filter_fields = ("name", "name__icontains")

    def create(self, request):
        name = request.data["name"]
        description = request.data["description"]
        image = request.data["image"]
        if isinstance(image, str):
            image_obj = ImageFile.objects.get(id=image)
        elif hasattr(image, "read"):
            image_obj = ImageFile(file=image)
            image_obj.save()
        else:
            raise ValueError("invalid image object")
        instance = FontImage(
            name=name,
            description=description,
            image=image_obj,
            create_time=datetime.now(),
            status=ImageStatus.init,
        )
        instance.save()
        return Response(self.get_serializer(instance).data)

    @action(["get"], detail=True)
    def image(self, request, **kwargs):
        self.filter_queryset
        instance: FontImage = self.get_object()
        return FileResponse(instance.image.file, filename=f"{instance.id}.jpeg")


class FontBlockView(ModelViewSet):
    model = FontBlock
    serializer_class = FontBlockSerializer
