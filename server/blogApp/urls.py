from django.urls import path
from .views import BlogViewSet

urlpatterns = [
    path('blogs/', BlogViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('blogs/<int:pk>/', BlogViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),
]
