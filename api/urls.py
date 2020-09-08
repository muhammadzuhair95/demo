from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewSet


router = DefaultRouter()

router.register('viewset', ViewSet, basename='viewset')

urlpatterns =[
    path('', include(router.urls))
]
