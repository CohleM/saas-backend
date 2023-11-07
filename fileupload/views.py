from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import File
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()
