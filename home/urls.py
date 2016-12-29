from django.conf.urls import url

from . import views

urlpatterns = [
	#home
	url(r'^$', views.index, name='index'),

	#interests
	url(r'archery/$', views.archery, name='archery'),
	url(r'cooking/$', views.cooking, name='cooking'),
	url(r'poker/$', views.poker, name='poker'),

	#projects
	url(r'projects/$', views.projects, name='projects'),
]
