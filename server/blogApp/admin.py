from django.contrib import admin
from .models import Blog, Category, Comment, Likes, PostViews

# Django admin panelinde görüntülemek istediğiniz modelleri kaydedin
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(PostViews)
