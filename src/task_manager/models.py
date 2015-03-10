from django.db import models
from university_dashboard.models import StudentGroup, Student
from django.utils import timezone

# Create your models here.
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
		return self.title + ': ' + self.description + '. Due on ' + str(self.dueDate)