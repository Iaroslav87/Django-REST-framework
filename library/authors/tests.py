from django.test import TestCase

# Create your tests here.
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorModelSerializer


class AuthorModelViewSet(ModelViewSet):
    """
    Класс набора представлений для модели Author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer