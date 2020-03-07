from django.urls import path
from rest_framework_mongoengine.routers import DefaultRouter

route = DefaultRouter()

urlpatterns = [
    path("", route.urls),
]
