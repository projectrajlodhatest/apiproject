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
from django.http import HttpResponse


def web_user(request):
    print('fuighhgihghgh')
    return HttpResponse("hello")