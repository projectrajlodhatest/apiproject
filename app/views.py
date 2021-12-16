from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from app import serializers
from app.serializers import StaffTeamSerializer,EmployeeSerializer,UserProfileSerializer,UserLoginSerializer,GetEmployeeSerializer
from .models import StaffTeam,Employee,UserProfile
from rest_framework.response import Response


from django.http import HttpResponse
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework.permissions import IsAuthenticated
from django.conf import settings





def index(request):
	print(request.META['HTTP_HOST'])
	return HttpResponse("Hello, world. You're at the polls index.")

class CreateStaffApi(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)            

	def post(self,request,*args,**kwargs):
		serializer = StaffTeamSerializer(data=request.data)
		if serializer.is_valid():
			user = User.objects.create_user(username='abcc')
			StaffTeam.objects.create(user=user,staff_name=serializer.data['staff_name'],staff_type=serializer.data['staff_type'])
			return Response(
				data={
				'suceess':True
				},
				status=status.HTTP_200_OK
			)	
		else:
			
			return Response(
				data={
				'errors':serializer.errors,
				'suceess':False
				},
			)	
	def get(self,request,*args,**kwargs):
		serializer_class = StaffTeamSerializer
		staff_objects = StaffTeam.objects.all()
		return Response(
				data={
					'staff_name':staff_objects[0].staff_name,
					'staff_type':staff_objects[0].staff_type,
					'success':True
				},
				status = status.HTTP_200_OK
			)
	def put(self,request,*args,**kwargs):
		serializer =StaffTeamSerializer(data=request.data)

		user= request.user
		if serializer.is_valid():
			staff_name =serializer.data['staff_name']
			staff_objects = StaffTeam.objects.all()
			obj=staff_objects[0]
			obj.staff_name = serializer.data['staff_name']
			obj.save()


		return Response(
			data={
			'success':True
			},
			status=status.HTTP_200_OK
			)
	def delete(self,request,*args,**kwargs):

		staff_obj =StaffTeam.objects.get(staff_name='it staff')
		staff_obj.delete()
		return Response(
			status=status.HTTP_204_NO_CONTENT
			) 	


class EmployeeStaffApi(generics.ListCreateAPIView):
	def post(self,request,*args,**kwargs):
		serializer = EmployeeSerializer(data=request.data)
		if serializer.is_valid():
			staff_obj = StaffTeam.objects.get(staff_name='it staff')
			print(staff_obj)
			Employee.objects.create(staff=staff_obj,employee_name=serializer.data['employee_name'],employee_address=serializer.data['employee_adress']
				,employee_phone=serializer.data['employee_phone'],employee_email=serializer.data['employee_email'],employee_zipcode=serializer.data['employee_zipcode'])
			return Response(
				data={
				'suceess':True
				},
				status=status.HTTP_200_OK
			)	
		else:
			
			return Response(
				data={
				'errors':serializer.errors,
				'suceess':False
				},
			)	

	def get(self,request,*args,**kwargs):
		emp_objects = Employee.objects.all()
		list_of_emp = []
		for each in emp_objects:
			list_of_emp.append({
				'employee_name':each.employee_name,
				'employee_address':each.employee_address,
				'employee_email':each.employee_email,
				'employee_phone':each.employee_phone,
				'employee_zipcode':each.employee_zipcode,

				})
		return Response(
			data={
				'list of employee':list_of_emp,
				'success':True
			},
			status = status.HTTP_200_OK
			)

class UserRegistration(generics.ListCreateAPIView):
	serializer = UserProfileSerializer
	def post(self,request,*args,**kwargs):
		serializer =UserProfileSerializer (data=request.data)
		print(serializer.is_valid())
		if serializer.is_valid():
			print(serializer.data)
			user =  User.objects.create_user(username='bhole',email=serializer.data['email'],password=serializer.data['password'])
			UserProfile.objects.create(user=user,address=serializer.data['address'],last_name=serializer.data['last_name'])
			return Response(
					data={
					'suceess':True
					},
					status=status.HTTP_200_OK
				)	
		else:
			
			return Response(
				data={
				'errors':serializer.errors,
				'suceess':False
				},
			)


class UserLogin(generics.ListCreateAPIView):
	serializer = UserLoginSerializer
	def post(self,request,*args,**kwargs):
		serializer=UserLoginSerializer(data=request.data)
		if serializer.is_valid():
			user = User.objects.get(email=serializer.data['email'])
			user = authenticate(request, username=user.username, password=serializer.data['password'])
			print(user)
			if user is not None:
				login(request,user)
				return Response(
					data={
					# 'username':user.username,
					# 'email':user.email,
					'suceess':True
					},
					status=status.HTTP_200_OK
				)	
		else:
			return Response(
				data={
				'errors':serializer.errors,
				'suceess':False
				},
			)


class Employees(generics.ListCreateAPIView):
	serializer =  StaffTeamSerializer()
	permission_classes = (IsAuthenticated,)             
	def get(request,self,*args,**kwargs):
		emp_obj =Employee.objects.all()
		serializer =  EmployeeSerializer(emp_obj,many=True)		# serializer = serializer(emp_obj)
		print(serializer.data)
		return Response(
			data={
				'list of employee':serializer.data,
				'success':True
			},
			status = status.HTTP_200_OK
			)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CustomAuthToken(ObtainAuthToken):

	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data,
										   context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		print(user)
		token, created = Token.objects.get_or_create(user=user)
		return Response({
			'token': token.key,
			'user_id': user.pk,
			'email': user.email
		})




from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def data_table(request):
	print(request)
	obj = Employee.objects.values('staff__staff_name','employee_name','employee_phone','employee_email')
	print(obj.count())
	data={}
	# obj=data.append(obj)
	# print(obj)
	data_list=[]
	for each in obj:
		data_list.append(each)

	from django.http import JsonResponse

	if request.method == 'POST':
		print('hfh')
		return JsonResponse(list(data_list),safe=False)   


	return render(request,'data_table.html')
from rest_framework.views import APIView
class Emp(APIView):
	def get(self,request,*args,**kwargs):		
		emp_obj= Employee.objects.all()
		serilizer=GetEmployeeSerializer(emp_obj,many=True)	
		return Response(
		data={
			'list of employee':serilizer.data,
			'success':True
		},
		status = status.HTTP_200_OK
		)

	def post(self,request,*args,**kwargs):
			serializer= EmployeeSerializer(data=request.data)
			print(serializer)
			if serializer.is_valid():
				obj=serializer.save()
				print(obj)
				return Response(
				data={
					'success':True
				},
				status = status.HTTP_200_OK
				)
			else:
				return Response(
				data={
					'list of employee':serializer.errors,
					'success':True
				},
				status = status.HTTP_200_OK
				)	
