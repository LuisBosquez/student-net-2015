from django.contrib import admin

# Register your models here.
from .models import University, StudentGroup

class UniversityAdmin(admin.ModelAdmin):
	class Meta:
		model = University

admin.site.register(University, UniversityAdmin)