# -*- encoding: utf-8 -*-
from rest_framework_mongoengine import serializers

from .models import FontBlock, FontImage


class FontImageSerializer(serializers.DocumentSerializer):
    class Meta:
        model = FontImage
        fields = "__all__"


class FontBlockSerializer(serializers.DocumentSerializer):
    class Meta:
        model = FontBlock
        fields = "__all__"
