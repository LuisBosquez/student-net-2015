from django.shortcuts import render
from university_dashboard.models import University, StudentGroup

# Create your views here.
def home(request):
	context = locals()
	template = 'index.html'
	return render(request, template, context)

def about(request):
	context = locals()
	template = 'about.html'
	return render(request, template, context)