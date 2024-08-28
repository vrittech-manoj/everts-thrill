from rest_framework.permissions import BasePermission
from accounts import roles

def IsAuthenticated(request):
    return bool(request.user and request.user.is_authenticated)

def AdminLevel(request):
    return bool(IsAuthenticated(request) and request.user.is_authenticated and request.user.role in [roles.ADMIN,roles.SUPER_ADMIN])

class AdminViewSetsPermission(BasePermission):
    def has_permission(self, request, view):
        # return True
        if view.action in ["list"]:
            return True
        elif view.action in ['retrieve']:
            return True
        elif view.action in ['create','update']:
            return True
            return ObjectBOwner(request) #third level
        elif view.action == "partial_update":
            return True
        elif view.action == 'destroy':
            return AdminLevel(request)