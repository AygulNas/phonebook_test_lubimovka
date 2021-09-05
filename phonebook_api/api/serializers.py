from rest_framework import serializers

from .models import Company, Employee, User


class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(
        slug_field='name',
        read_only=False,
        queryset=Company.objects.all(),
    )

    def validate(self, value):
        if (not value['phone_number'] and
           not value['office_number'] and
           not value['fax_number']):
            raise serializers.ValidationError('Enter telefon number')
        if (value['phone_number'] and
           Employee.objects.filter(phone_number=value['phone_number'])):
            raise serializers.ValidationError('Enter unique Phone_number')
        return value

    class Meta:
        model = Employee
        fields = ('lastname', 'firstname', 'secondname', 'position',
                  'phone_number', 'office_number', 'fax_number', 'company')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username')


class CompanySerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=True, read_only=True)
    creator = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    moderator = UserSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        fields = ('__all__')
        model = Company
