from django import forms
from .models import Task
from django.utils import timezone

class createTaskForm(forms.Form):
	title = forms.CharField(required = True, max_length = 100, help_text='Task title')
	description = forms.CharField(required = True, help_text='Description')
	dueDate = forms.DateTimeField(required = True, help_text='Due Date', initial = timezone.now())
	status = forms.BooleanField(help_text='Status', initial = False)
	type = forms.ChoiceField(choices = Task.TASK_TYPE_CHOICES, required = True)