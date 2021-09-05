from .serializers import (CompanySerializer, EmployeeSerializer)
from rest_framework.viewsets import ModelViewSet
from .models import Company, Employee
from .permissions import IsAllowedChangeCompanies
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class CompanyViewSet(ModelViewSet):
    permission_classes = [IsAllowedChangeCompanies]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name', 'employee__lastname',
                     'employee__firstname', 'employee__secondname',
                     'employee__position', 'employee__phone_number',
                     'employee__office_number',  'employee__fax_number',)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
