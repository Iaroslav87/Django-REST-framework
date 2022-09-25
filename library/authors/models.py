from django.db import models
from uuid import uuid4

class Author(models.Model):
    """
    Класс Автор
    Общая, простая модель автора книги
    ----------------------------------
    uid - первичный ключ, UUID
    first_name - текст (макс.длина 64 символа)
    last_name - текст (макс.длина 64 символа)
    birthday_year - натуральное число
    ----------------------------------
    """
    uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()