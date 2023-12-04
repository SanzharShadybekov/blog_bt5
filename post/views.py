from rest_framework import generics, permissions

from post import serializers
from post.models import Post
from post.persmissions import IsOwner, IsOwnerOrAdmin


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.PostListSerializer
        return serializers.PostCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return serializers.PostCreateUpdateSerializer
        return serializers.PostDetailSerializer

    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH'):
            return [permissions.IsAuthenticated(), IsOwner()]
        elif self.request.method == 'DELETE':
            return [IsOwnerOrAdmin()]
        return [permissions.AllowAny()]
