from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель, представляющая группу, к которой могут принадлежать посты.

    Группа содержит название, уникальный слаг и описание.
    Посты можно организовать по группам для удобства работы с контентом.
    """

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        """Возвращает строковое представление группы."""
        return self.title


class Post(models.Model):
    """Модель, представляющая пост пользователя.

    Каждый пост содержит текст, дату публикации, автора,
    необязательное изображение и может принадлежать группе.
    """

    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )

    def __str__(self):
        """Возвращает строковое представление поста."""
        return self.text


class Comment(models.Model):
    """Модель, представляющая комментарий к посту.

    Комментарии связаны с автором и постом, к которому они принадлежат,
    и включают текст и дату создания.
    """

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )
