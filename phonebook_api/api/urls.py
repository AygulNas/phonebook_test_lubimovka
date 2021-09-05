from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'company', views.CompanyViewSet, basename='company')
router.register(r'employee', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('v1/', include(router.urls)),
]
