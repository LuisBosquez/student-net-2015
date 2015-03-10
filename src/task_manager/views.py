from django.shortcuts import render
from django.shortcuts import redirect

from .forms import createTaskForm
# Create your views here.

def createTask(request):
	form = createTaskForm(request.POST or None)
	if form.is_valid():
		print (request.POST)
		return redirect('tasks')
	
	context = locals()
	template = 'create-task.html'
	return render(request, template, context)