from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'university_dashboard.views.home', name='home'),
	url(r'^about/', 'university_dashboard.views.about', name='about'),
	url(r'^calendar/', 'university_dashboard.views.calendar', name='calendar'),
	url(r'^validate/', 'university_dashboard.views.validate', name='validate'),
	url(r'^groups/', 'university_dashboard.views.groups', name='groups'),
	url(r'^members/', 'university_dashboard.views.members', name='members'),
	url(r'tasks/$', 'university_dashboard.views.tasks', name='tasks'),
	
	url(r'^tasks/new/$', 'task_manager.views.createTask', name='createTask'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)