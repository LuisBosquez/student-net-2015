from django.shortcuts import render
from university_dashboard.models import University, StudentGroup
from task_manager.models import Task

# Create your views here.
def home(request):
	context = locals()
	template = 'index.html'
	return render(request, template, context)

def about(request):
	context = locals()
	template = 'about.html'
	return render(request, template, context)
	
def calendar(request):
	context = locals()
	template = 'calendar.html'
	return render(request, template, context)
	
def groups(request):
	context = locals()
	template = 'groups.html'
	return render(request, template, context)

def members(request):
	context = locals()
	template = 'members.html'
	return render(request, template, context)
	
def tasks(request):
	context = {'title':'Tareas', 'tasks':Task.objects.all()}
	template = 'tasks.html'
	return render(request, template, context)