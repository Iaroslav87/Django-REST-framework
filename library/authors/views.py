from email.policy import default
from typing import Generic
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.pagination import LimitOffsetPagination
from .models import Author, Biography, Book, Article
from .serializers import AuthorModelSerializer, BiographyModelSerializer, ArticleModelSerializer, BookModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    """
    Настройки пагинатора для проекта
    """
    default_limit = 3


class AuthorSpecialViewSet(
    GenericViewSet, 
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
):
    """
    Класс набора представлений для модели Author.
    Реализованы методы CRUD.
    """
    queryset = Author.objects.all()
    renderer_class = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = AuthorModelSerializer
    filterset_fields = ['last_name', 'first_name']
    pagination_class = ProjectLimitOffsetPagination


class BiographySpecialViewSet(
    GenericViewSet,
    CreateModelMixin, 
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
):
    """
    Класс набора представлений для модели Biography.
    Реализованы все  методы CRUD.
    """
    queryset = Biography.objects.all()
    renderer_class = [JSONRenderer, BrowsableAPIRenderer,]
    serializer_class = BiographyModelSerializer
    filterset_fields = ['author']
    pagination_class = ProjectLimitOffsetPagination


class ArticleSpecialViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
):
    """
    Класс набора представлений для модели Article.
    Реализованы все методы CRUD.
    """
    queryset = Article.objects.all()
    renderer_class = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = ArticleModelSerializer
    filterset_field = ['author',]
    pagination_class = ProjectLimitOffsetPagination


class BookSpecialViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
):
    """
    Класс набора представлений для модели Book.
    Реализованы все методы CRUD.
    """
    queryset = Book.objects.all()
    renderer_class = [JSONRenderer,BrowsableAPIRenderer]
    serializer_class = BookModelSerializer
    filterset_field = ['author']
    pagination_clas = ProjectLimitOffsetPagination