from rest_framework import serializers
from app.models import *
class StaffTeamSerializer(serializers.Serializer):
	staff_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
	staff_type = serializers.CharField(required=False, allow_blank=True, max_length=100)

class EmployeeSerializer(serializers.Serializer):
	staff = serializers.IntegerField(source="staff_id")
	employee_name = serializers.CharField(required=False,allow_blank=True,max_length=100)
	employee_adress = serializers.CharField(required=False,allow_blank=True)
	employee_phone = serializers.CharField(required =False,allow_blank=True,max_length=100)
	employee_email = serializers.CharField(required =False,allow_blank=True,max_length=256)
	employee_zipcode = serializers.CharField(required=False)
	def create(self,validated_data):
		obj =Employee.objects.create(**validated_data)
		return obj	


class UserProfileSerializer(serializers.Serializer):
	address = serializers.CharField(required=False)
	email= serializers.CharField(required=False)
	last_name= serializers.CharField(required=False)
	password =  serializers.CharField(required=False)	

class UserLoginSerializer(serializers.Serializer):
	email = serializers.CharField(required=False)
	password =  serializers.CharField(required=False)

class GetEmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields="__all__"