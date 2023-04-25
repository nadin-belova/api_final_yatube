from rest_framework import viewsets
from posts.models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset 
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
