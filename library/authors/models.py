from django.db import models
from uuid import uuid4

class Author(models.Model):
    """
    Класс Автор.
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

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    
class Biography(models.Model):
    """
    Класс Биография.
    Простая модель биографии автора, содержит связь one-to-one с классом автора
    (биография автора)
    ---------------------------------
    """
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    """
    Класс Книга.
    Простая модель книги, содержит связь many-to-many с классом автора
    (может быть написана несколькими авторами)
    """
    book_name = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)


class Article(models.Model):
    """
    Класс Статья.
    Модель статьи, содержит внешний ключ для связи с конкретным автором
    (статья написана автором)
    """
    article_name = models.CharField(max_length=64)
    author = models.ForeignKey(Author, models.PROTECT)