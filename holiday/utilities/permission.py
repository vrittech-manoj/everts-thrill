from rest_framework.permissions import BasePermission
from accounts import roles

def IsAuthenticated(request):
    return bool(request.user and request.user.is_authenticated)

def AdminLevel(request):
    return bool(IsAuthenticated(request) and request.user.is_superuser and request.user.role in [roles.ADMIN,roles.SUPER_ADMIN])

class AdminViewSetsPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create','update','partial_update','delete']:
            return AdminLevel(request)
        elif view.action in ['list','retrieve']:
            return True
        