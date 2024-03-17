from rest_framework import serializers
from .models import Blog, Category, Comment, Likes, PostViews

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    total_comments = serializers.SerializerMethodField(read_only=True)
    total_likes = serializers.SerializerMethodField(read_only=True)
    total_views = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'

    def get_total_comments(self, obj):
        return obj.comments.count()

    def get_total_likes(self, obj):
        return obj.likes.count()

    def get_total_views(self, obj):
        return obj.views.count()
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)


class UserBlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Blog
        exclude = ('status',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'

class PostViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostViews
        fields = '__all__'

