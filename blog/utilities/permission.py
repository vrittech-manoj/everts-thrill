from rest_framework.permissions import BasePermission
from accounts import roles

def IsAuthenticated(request):
    return bool(request.user and request.user.is_authenticated)

def AdminLevel(request):
    return bool(IsAuthenticated(request) and request.user.is_authenticated and request.user.role in [roles.ADMIN,roles.SUPER_ADMIN])

class AdminViewSetsPermission(BasePermission):
    def has_permission(self, request, view):
        True
        if view.action in ["list"]:
            return True
        elif view.action in ['retrieve']:
            return AdminLevel(request)
        elif view.action in ['create','update']:
            return AdminLevel(request) #second level
            return ObjectBOwner(request) #third level
        elif view.action == "partial_update":
            return AdminLevel(request)
        elif view.action == 'destroy':
            return AdminLevel(request)
