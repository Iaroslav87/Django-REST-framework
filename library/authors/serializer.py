from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author


class AuthorModelSerializer(HyperlinkedModelSerializer):
    """
    Сериализатор для модели Author,
    наследуется от HyperlinkedModelSerializer,
    """
    class Meta:
        model = Author
        fields = '__all__'