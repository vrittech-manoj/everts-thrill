"""
URL configuration for cnex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

from  rest_framework  import routers

from accounts.urls import router as accounts_router
from blog.urls import router as blog_router
from booking.urls import router as booking_router
from holiday.urls import router as holiday_router
from managements.urls import router as managements_router
from payment.urls import router as payment_router
from queries.urls import router as queries_router
from services.urls import router as services_router
from testonomial.urls import router as testonomial_router
from holiday.routers.routers import router as holiday_router
from activities.routers.routers import router as activities_router
from collection.routers.routers import router as collection_router
from destination.routers.routers import router as destination_router

router = routers.DefaultRouter()

router.registry.extend(accounts_router.registry)
router.registry.extend(blog_router.registry)
router.registry.extend(booking_router.registry)
router.registry.extend(holiday_router.registry)
router.registry.extend(managements_router.registry)
router.registry.extend(payment_router.registry)
router.registry.extend(queries_router.registry)
router.registry.extend(services_router.registry)
router.registry.extend(testonomial_router.registry)

schema_view = get_schema_view(
   openapi.Info(
      title="Trek Ecommerce API",
      default_version='v1',
      description="Trek Ecommerce System",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="manojdas.py@gmail.com"),
      license=openapi.License(name="No License"),
      **{'x-logo': {'url': 'your-logo-url'}},
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path('', lambda request: HttpResponse("cdn storage fixing"), name='index'),
    path('api/',include(router.urls)),
    path('api/accounts/',include('accounts.urls')),
    path('api/blogs/',include('blog.urls')),
    path('api/booking/',include('booking.urls')),
    path('api/holiday/',include('holiday.urls')),
    path('api/services/',include('services.urls')),
    path('api/testonomial/',include('testonomial.urls')),
    path('api/queries/',include('queries.urls')),
    path('api/managements/',include('managements.urls')),
    path('api/',include('accountsmanagement.urls')),
    path('api/',include(destination_router.urls)),
    path('api/',include(collection_router.urls)),
    path('api/',include(activities_router.urls)),
    path('api/',include(holiday_router.urls)),
    

    #path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
