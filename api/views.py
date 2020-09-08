from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.

class ViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        return Response({'method':'Create method is called'}, status.HTTP_200_OK)


    def list(self, request):
        return Response({'method':'List method is called'}, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        return Response({'method': 'Retrieve method is called'}, status.HTTP_200_OK)

    def update(self, request, pk=None):
        return Response({'method':'Update method is called'}, status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        return Response({'method':'Destroy method is called'}, status.HTTP_200_OK)
