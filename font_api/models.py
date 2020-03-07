# -*- encoding: utf-8 -*-
from enum import IntEnum

import mongoengine
from django.db import models

# Create your models here.
# todo: 增加索引


class ImageFile(mongoengine.Document):
    file = mongoengine.ImageField()


class ImageStatus(IntEnum):
    init = 0
    detect_block = 1
    detect_block_failed = 2
    detect_block_finish = 3
    detect_font = 4
    detect_font_finish = 5


class FontImage(mongoengine.Document):
    """一个图片文件"""

    name = mongoengine.StringField(default="")
    description = mongoengine.StringField(default="")
    image = mongoengine.ReferenceField(ImageFile)
    create_time = mongoengine.DateTimeField()

    CHOICES = [(item.value, item.name) for item in ImageStatus]
    status = mongoengine.IntField(choices=CHOICES)


class RectPoint(mongoengine.EmbeddedDocument):
    x = mongoengine.FloatField()
    y = mongoengine.FloatField()

    def __str__(self):
        return f"<RectPoint x={self.x} y={self.y} >"


class ProbFont(mongoengine.EmbeddedDocument):
    """每个框选的文字可能的字体"""

    name = mongoengine.StringField()
    weight = mongoengine.StringField()


class FontBlock(mongoengine.Document):
    """存放图像中的文字框"""

    font_image_id = mongoengine.StringField()
    source = mongoengine.StringField()
    points = mongoengine.EmbeddedDocumentListField(RectPoint)
    text = mongoengine.StringField(default="")
    user_select = mongoengine.StringField(default="")  # 存放人工选中字体的 name
    fonts = mongoengine.EmbeddedDocumentListField(ProbFont)  # 可能的字体


mongoengine.connect(db="FontDb", host="mongodb://127.0.0.1:27017")
