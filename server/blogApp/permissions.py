from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Kullanıcı admin ise veya blogun sahibi ise izin ver
        return request.user.is_staff or obj.user == request.user
    
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        #get işlemini her kullanıcı yapabilecek update ve delete işlemlerini yalnızca blog sahibi ve staff user
        if request.method == 'GET':
            return True 
        return bool(obj.user == request.user or request.user.is_staff)