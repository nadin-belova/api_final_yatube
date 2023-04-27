from rest_framework import viewsets
from posts.models import Post, Comment, Group, Follow
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer)
from django.shortcuts import get_object_or_404
from rest_framework import pagination, permissions, viewsets
from .permissions import OwnerOrReadOnly
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = (OwnerOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, post_id=self.kwargs['post_id'])

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    pagination_class = pagination.LimitOffsetPagination
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username', 'user__username',)

    def get_queryset(self):
        """Возвращает все подписки пользователя, сделавшего запрос"""
        qs = Follow.objects.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        following = serializer.validated_data['following']
        if following == self.request.user:
            raise ValidationError("Нельзя подписаться на самого себя")
        # Проверяем, не подписан ли уже пользователь на данного автора
        if Follow.objects.filter(user=self.request.user,
                                 following=following).exists():
            raise ValidationError("Вы уже подписаны на этого автора")

        serializer.save(user=self.request.user)
