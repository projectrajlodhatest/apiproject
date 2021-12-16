from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.db.models.signals import post_save,pre_save


class StaffTeam(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	staff_name = models.CharField(max_length=30)
	staff_type= models.CharField(max_length=10)
	create_date =models.DateTimeField(auto_now=True)


class Employee(models.Model):
	staff = models.ForeignKey(StaffTeam,on_delete=models.CASCADE)	
	employee_name = models.CharField(max_length=40,null=True)
	employee_address = models.CharField(max_length=256,null=True)
	employee_phone = models.CharField(max_length=256,null=True)
	employee_email = models.CharField(max_length=256)
	employee_zipcode = models.CharField(max_length=256)

class UserProfile(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	address= models.CharField(max_length=200)
	last_name = models.CharField(max_length=100)

def save_post(sender,instance,**kwargs):
	print('working fine')


post_save.connect(save_post,sender=UserProfile)	

 

class MyModel(models.Model):

	# file will be uploaded to MEDIA_ROOT / uploads
	upload = models.ImageField(upload_to ='uploads/')

	# or...
	# file will be saved to MEDIA_ROOT / uploads / 2015 / 01 / 30
	upload = models.ImageField(upload_to ='upload')





class common(models.Model): # COMM0N
	name = models.CharField(max_length=100)

	class Meta:
		abstract = True


class Student(common): # STUDENT
	rollno = models.IntegerField()


class Teacher(common): # TEACHER
	num = models.IntegerField()

class Student2(common):
	last_name=models.CharField(max_length=100)	
	class Meta:
		abstract=True



class Place(models.Model):
	name=models.CharField(max_length=20)
	address=models.TextField(max_length=20)

	def __str__(self):
		return self.name


class Restaurants(Place):
	serves_pizza=models.BooleanField(default=False)
	serves_pasta=models.BooleanField(default=False)

class SampleManger(models.Model):
	name=models.CharField(max_length=100)
	age=models.IntegerField()	
	objects=models.Manager()
	obj=models.Manager()





