from django.db import models
from django.utils import timezone

# Create your models here, yo!

class University(models.Model):
	SUPPORTED_LANGUAGES_CHOICES = (
		('EN', 'English'),
		('ES', 'Spanish'),
		('FR', 'French')
	)
	
	name = models.CharField(max_length = 200)
	location = models.CharField(max_length = 200)
	language = models.CharField(max_length = 2, choices = SUPPORTED_LANGUAGES_CHOICES)
	memberSince = models.DateTimeField('date joined', default=timezone.now())
	
	def __str__(self):
		return  self.name

class StudentGroup(models.Model):
	university_id = models.ForeignKey(University)
	name = models.CharField(max_length = 200)
	size = models.IntegerField(default = 0)
	category = models.CharField(max_length = 200, default="None specified")
	memberSince = models.DateTimeField('date joined', default=timezone.now())
	
	def __str__(self):
		return self.name
	