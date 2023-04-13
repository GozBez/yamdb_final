from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import year_validator

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Жанр'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(
        Category, related_name='titles', on_delete=models.SET_NULL, null=True
    )
    genre = models.ManyToManyField(Genre, through='GenreTitle')
    year = models.IntegerField(validators=[year_validator])
    description = models.TextField(blank=True, default='Для описания')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Произведение'

    def __str__(self):
        return f'{self.name}{self.genre}'


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'id {self.pk} жанр {self.genre}  title  {self.title}'


class Review(models.Model):
    """Отзывы на произведения"""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )
    text = models.TextField()
    score = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)


class Meta:
    ordering = ('pub_date',)
    verbose_name = 'Отзыв'
    constraints = [
        models.UniqueConstraint(
            fields=['author', 'title'],
            name='unique_author_review'
        )
    ]


def __str__(self):
    return self.text


class Comment(models.Model):
    """Комментарии к отзывам"""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Комментарий'

    def __str__(self):
        return self.text[:16]
