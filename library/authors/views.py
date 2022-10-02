from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Author, Biography, Book, Article
from .serializers import AuthorModelSerializer, BiographyModelSerializer, ArticleModelSerializer, BookModelSerializer


class AuthorModelViewSet(ModelViewSet):
    """
    Класс набора представлений для модели Author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BiographyModelViewSet(ModelViewSet):
    """
    Класс набора представлений для модели Biography
    """
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class ArticleModelViewSet(ModelViewSet):
    """
    Класс набора представлений для модели Article
    """
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class BookModelViewSet(ModelViewSet):
    """
    Класс набора представлений для модели Book
    """
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer