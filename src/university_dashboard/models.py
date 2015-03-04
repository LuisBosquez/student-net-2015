from django.db import models
from django.utils import timezone

# Create your models here, yo!

class University(models.Model):
	SUPPORTED_LANGUAGE_CHOICES = (
		('EN', 'English'),
		('ES', 'Spanish'),
		('FR', 'French')
	)
	
	name = models.CharField(max_length = 200)
	location = models.CharField(max_length = 200)
	language = models.CharField(max_length = 2, choices = SUPPORTED_LANGUAGE_CHOICES)
	memberSince = models.DateTimeField('date joined', default = timezone.now())
	
	def __str__(self):
		return  self.name

class StudentGroup(models.Model):
	STUDENT_GROUP_CATEGORY_CHOICES = (
		('MJ', 'Major'),
		('RA', 'Recreational Activty'),
		('MS', 'Miscellaneous')
		
	)
	
	university = models.ForeignKey(University)
	
	name = models.CharField(max_length = 200)
	description = models.TextField('Description')
	category = models.CharField(max_length = 200, default="None specified", choices = STUDENT_GROUP_CATEGORY_CHOICES)	
	
	memberSince = models.DateTimeField('date joined', default=timezone.now())
	
	def __str__(self):
		return self.name
	
class Student:
	STUDENT_MAJOR_CHOICES = (
		('CS', 'Computer Science'),
		('EC', 'Economics'),
		('FI', 'Finance'),
		('MK', 'Marketing')
	)
	university = models.ForeignKey(University)
	studentGroup = models.ForeignKey(StudentGroup)
	
	name = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	major = models.CharField(max_length = 200, choices = STUDENT_MAJOR_CHOICES)
	
	def __str__(self):
		return self.name

class Task:
	studentGroup = models.ForeignKey(StudentGroup)
	
	
	title = models.CharField(max_length = 200)
	description = models.TextField('Description')
	