from django.db import models
from django.utils import timezone

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
	
	def __str__(self):
		return self.name

class Task(models.Model):
	TASK_TYPE_CHOICES = (
		('WP', 'Work Plan'),
		('UR', 'University Requirement'),
		('IT','Internal Task')
	)
	studentGroup = models.ForeignKey(StudentGroup)
	assignedTo = models.ManyToManyField(Student)
	
	title = models.CharField(max_length = 200)
	description = models.TextField('Description', blank=True)
	dueDate = models.DateTimeField('Due Date', default = timezone.now())
	dateCreated = models.DateTimeField('Date Created', default = timezone.now())
	status = models.BooleanField('Status', default = False)
	type = models.CharField(max_length = 200, choices = TASK_TYPE_CHOICES)
	
	def __str__(self):
		return self.title + ': ' + self.description + '. Due on ' + dueDate