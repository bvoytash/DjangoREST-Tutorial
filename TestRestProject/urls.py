
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from TestRestProject.Customer.views import CustomerViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
