from rest_framework.permissions import BasePermission
from . import roles

def IsAuthenticated(request):
    print(request.user)
    return bool(request.user and request.user.is_authenticated)

def ownerPermission(request,view,label):
    if request.user.role in [roles.ADMIN,roles.SUPER_ADMIN]:
        return True
    
    payload_user = view.get_object()
    print(payload_user,label,request.user.id)
    if request.user.id == payload_user.id:
        return True
    else:
        False

def AdminPermission(request):
    return IsAuthenticated(request) and request.user.role in [roles.ADMIN, roles.SUPER_ADMIN]

class AccountPermission(BasePermission):
    def has_permission(self, request, view):
        method_name = view.action
        if method_name in ['list', 'create', 'retrieve']:
            return True
        elif method_name == 'partial_update':
            return ownerPermission(request,view,'id')
        elif method_name == 'update':
            return IsAuthenticated(request) and ownerPermission(request,view,'id')
        else:
            return False


class AdminLevelPermission(BasePermission):
    def has_permission(self, request, view):
        method_name = view.action
        if method_name in ['create', 'retrieve', 'update', 'partial_update']:
            return AdminPermission(request)
        elif method_name == 'list':
            return True
        else:
            return False


class AllUserDataPermission(BasePermission):
    def has_permission(self, request, view):
        method_name = view.action
        # print(method_name)
        return AdminPermission(request) if method_name == 'list' else False

    