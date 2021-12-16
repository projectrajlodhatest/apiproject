from django.urls import path

from . import views
from.import web
from .views  import CreateStaffApi,EmployeeStaffApi,UserRegistration,UserLogin,Employees,CustomAuthToken,Emp

urlpatterns = [
    path('', views.index, name='index'),
    path('staff',CreateStaffApi.as_view(),name='staff'),
    path('employee-staf',EmployeeStaffApi.as_view(),name='employee_staff'),
    path('user-profile',UserRegistration.as_view(),name='user_profile'),
    path('user-login',UserLogin.as_view(),name='user_login'),
    path('employee',Employees.as_view(),name='employee'),
    path('token',CustomAuthToken.as_view()),
    path('data_table',views.data_table,name='data_table'),
    path('emp',Emp.as_view(),name='emp'),
    path('web',web.web_user,name='web')

]