from rest_framework import serializers

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post.

    Обрабатывает сериализацию и десериализацию объектов Post,
    включая все базовые поля с автором, доступным только для чтения.
    """

    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        """Метаданные для PostSerializer."""

        model = Post
        fields = ('__all__')
        read_only_fields = ['author']


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group.

    Обеспечивает сериализацию всех полей модели Group.
    """

    class Meta:
        """Метаданные для GroupSerializer."""

        model = Group
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment.

    Обрабатывает сериализацию всех полей модели Comment.
    """

    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        """Метаданные для CommentSerializer."""

        model = Comment
        fields = ('__all__')
        read_only_fields = ['author', 'post']
