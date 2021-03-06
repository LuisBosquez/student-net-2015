from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here, yo!

class University(models.Model):
	SUPPORTED_LANGUAGE_CHOICES = (
		('EN', 'English'),
		('ES', 'Spanish'),
		('FR', 'French')
	)
	
	name = models.CharField(max_length = 200, default = "Some university")
	location = models.CharField(max_length = 200)
	language = models.CharField(max_length = 2, choices = SUPPORTED_LANGUAGE_CHOICES)
	memberSince = models.DateTimeField('Date Joined', default = timezone.now())
	
	def __str__(self):
		return  self.name

class StudentGroup(models.Model):
	STUDENT_GROUP_CATEGORY_CHOICES = (
		('MJ', 'Major'),
		('RA', 'Recreational Activty'),
		('MS', 'Miscellaneous')
		
	)
	
	university = models.ForeignKey(University)
	
	name = models.CharField(max_length = 200, default = "Some student group name")
	description = models.TextField('Description', default = "Some student group")
	category = models.CharField(max_length = 200, default="None specified", choices = STUDENT_GROUP_CATEGORY_CHOICES)	
	
	memberSince = models.DateTimeField('Date Joined', default=timezone.now())
	
	def __str__(self):
		return self.name
	
class Student(models.Model):
	STUDENT_MAJOR_CHOICES = (
		('CS', 'Computer Science'),
		('EC', 'Economics'),
		('FI', 'Finance'),
		('MK', 'Marketing')
	)
	university = models.ForeignKey(University)
	studentGroup = models.ForeignKey(StudentGroup)
	
	name = models.CharField(max_length = 200, default="Some student")
	email = models.CharField(max_length = 200, default = "email@university.edu")
	major = models.CharField(max_length = 200, choices = STUDENT_MAJOR_CHOICES)
	profile_picture = models.ImageField(upload_to='thumbpath', blank=True)
	
	def __str__(self):
		return self.name