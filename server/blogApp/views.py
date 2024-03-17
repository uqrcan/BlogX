from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrAdmin,IsOwnerOrReadOnly
from .models import Blog, Category, Comment, Likes, PostViews
from .serializers import BlogSerializer, UserBlogSerializer, CommentSerializer, LikesSerializer, PostViewsSerializer,CategorySerializer
from django.db.models import F

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return BlogSerializer
        return UserBlogSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy','PATCH']:
            permission_classes = [IsAdminUser, IsOwnerOrAdmin]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    def get(self, request, *args, **kwargs):
        blog_id = kwargs.get('blog_id')
        blog = get_object_or_404(Blog, pk=blog_id)
        post_views, created = PostViews.objects.get_or_create(blog=blog, user=request.user)
        if created:
            blog.views += 1
            blog.save()
        serializer = BlogSerializer(blog)
        return Response(serializer.data)



    def perform_create(self, serializer):
        category_id = serializer.validated_data.get('category')
        category = get_object_or_404(Category, id=category_id)
        serializer.save(user=self.request.user, category=category)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # partial=True olarak değiştirildi
        serializer.is_valid(raise_exception=True)
        category_id = serializer.validated_data.get('category')
        category = get_object_or_404(Category, id=category_id)
        serializer.save(user=self.request.user, category=category)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostViewsViewSet(viewsets.ModelViewSet):
    queryset = PostViews.objects.all()
    serializer_class = PostViewsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Yorum ve Beğeni işlemleri için yetkilendirme kontrolleri
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'update':
            self.permission_classes = [IsOwnerOrAdmin]
        return super().get_permissions()

class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

    def get_permissions(self):
        if self.action == 'update':
            self.permission_classes = [IsOwnerOrAdmin]
        return super().get_permissions()

#Görüntülenme işlemleri
