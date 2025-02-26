from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from TestRestProject.Customer.views import CustomerViewSet, DocumentViewSet, ProfessionViewSet, DataSheetViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'professions', ProfessionViewSet)
router.register(r'data_sheets', DataSheetViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
]