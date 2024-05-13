
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employess', EmployeeViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
#companies/[companyid]/employess