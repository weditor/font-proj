from django.urls import path, include
from rest_framework_mongoengine.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register("file", views.FileView, "file")
route.register("image", views.FontImageView, "image")
route.register("block", views.FontBlockView, "block")

urlpatterns = [
    path("", include(route.urls)),
]
