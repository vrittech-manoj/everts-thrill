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
from destination.urls import router as destination_router
from managements.urls import router as managements_router
# from payment.urls import router as payment_router
from queries.urls import router as queries_router
from services.urls import router as services_router
from destination.routers.routers import router as destination_router
from activities.routers.routers import router as activities_router
from collection.routers.routers import router as collection_router
from faqs.routers.routers import router as faqs_router
from departure.routers.routers import router as departure_router
from booking.routers.routers import router as booking_router
from company.routers.routers import router as company_router
from review.routers.routers import router as review_router
from airlines.routers.routers import router as airlines_router
from trek.utilities.bulk_upload import BulkUploadAPIView
from gallery.routers.routers import router as gallery_router

from trek.utilities.bulk_delete import BulkDelete

router = routers.DefaultRouter()

router.registry.extend(accounts_router.registry)
router.registry.extend(blog_router.registry)
router.registry.extend(destination_router.registry)
router.registry.extend(managements_router.registry)
# router.registry.extend(payment_router.registry)
router.registry.extend(queries_router.registry)
router.registry.extend(services_router.registry)
router.registry.extend(airlines_router.registry)
router.registry.extend(departure_router.registry)
router.registry.extend(review_router.registry)
router.registry.extend(booking_router.registry)
router.registry.extend(faqs_router.registry)
router.registry.extend(collection_router.registry)
router.registry.extend(activities_router.registry)
router.registry.extend(company_router.registry)
router.registry.extend(gallery_router.registry)
router.registry.extend(gallery_router.registry)


schema_view = get_schema_view(
   openapi.Info(
      title="Everest Thrill API",
      default_version='v1',
      description="Everest Thrill Trekking System",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="prashantkarna21@gmail.com"),
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
    path('api-auth/', include('rest_framework.urls')),
    path('api/accounts/',include('accounts.urls')),
    path('api/',include('blog.urls')),
    path('api/',include('destination.urls')),
    path('api/services/',include('services.urls')),
    path('api/queries/',include('queries.urls')),
    # path('api/managements/',include('managements.urls')),
    path('api/',include('accountsmanagement.urls')),
    path('api/',include(collection_router.urls)),
    path('api/',include(activities_router.urls)),
    path('api/',include(destination_router.urls)),
    path('api/',include(faqs_router.urls)),
    path('api/bulk-delete/<str:delete_type>/',BulkDelete.as_view(),name="bulk_delete"),
    path('api/',include(departure_router.urls)),
    path('api/',include(company_router.urls)),
    path('api/',include(booking_router.urls)),
    path('api/',include(review_router.urls)),
    path('api/',include(airlines_router.urls)),
    path('api/',include('dashboard.urls')),
    path('api/report/',include('report.urls')),
    
    path('api/bulk-upload/', BulkUploadAPIView.as_view(), name='bulk-upload'),

    #path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
