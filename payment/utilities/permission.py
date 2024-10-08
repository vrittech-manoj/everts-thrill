from rest_framework.permissions import BasePermission
from accounts import roles
from booking.models import DestinationBook

def IsAuthenticated(request):
    return bool(request.user and request.user.is_authenticated)

def AdminLevel(request):
    return bool(IsAuthenticated(request) and request.user.is_authenticated and request.user.role in [roles.ADMIN,roles.SUPER_ADMIN])

def isOwner(request):
    order = DestinationBook.objects.filter(id = request.data.get('order_id'))
    print(order, " permission ")
    if not order.exists():
        return False
    if request.user.id == order.first().user.id:
        return True
    return False


def isServiceOwner(request):
    order = DestinationBook.objects.filter(id = request.data.get('order_id'))
    print(order, " permission ")
    if not order.exists():
        return False
    if request.user.id == order.first().user.id:
        return True
    return False
    
class AdminViewSetsPermission(BasePermission):
    def has_permission(self, request, view):
        return AdminLevel(request)

class PaymentVerifyPermission(BasePermission):
    def has_permission(self, request, view):
        return IsAuthenticated(request) and isOwner(request)
        
class ServicePaymentVerifyPermission(BasePermission):
    def has_permission(self, request, view):
        return IsAuthenticated(request) and isServiceOwner(request)
        