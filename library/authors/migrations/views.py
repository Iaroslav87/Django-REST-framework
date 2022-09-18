from django.shortcuts import render

# Create your views here.

from .serializers import AuthorModelSerializer
from .models import Author
class AuthorModelViewSet(ModelViewSet):
    authors = Author.objects.all()
