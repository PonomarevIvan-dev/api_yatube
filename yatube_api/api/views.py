from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated
)
from django.shortcuts import get_object_or_404
from posts.models import Post, Group

from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для обработки операций с постами."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """Устанавливает текущего пользователя автором при создании поста."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для обработки операций с группами."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для обработки операций с комментариями, фильтруемых по посту."""

    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Возвращает комментарии, отфильтрованные по post_pk из URL."""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def get_object(self):
        """Возвращает комментарий, отфильтрованный по comment_id из URL."""
        queryset = self.get_queryset()
        comment_id = self.kwargs.get('pk')
        obj = get_object_or_404(queryset, id=comment_id)
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        """Создаёт объект с автором-юзером и привязывает к посту."""
        post_id = self.kwargs.get('post_id')
        serializer.save(
            author=self.request.user,
            post_id=post_id
        )
