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
	url(r'projects/highlights/$', views.projectHighlights, name='projectHighlights'),


	#food categories
	url(r'cooking/highlights/$', views.highlights, name='highlights'),
	url(r'cooking/breakfast/$', views.breakfast, name='breakfast'),
	url(r'cooking/stock/$', views.stock, name='stock'),
	url(r'cooking/fastCooking/$', views.fastCooking, name='fastCooking'),
	url(r'cooking/salads/$', views.salads, name='salads'),
	url(r'cooking/groundMeat/$', views.groundMeat, name='groundMeat'),
	url(r'cooking/roasts/$', views.roasts, name='roasts'),
	url(r'cooking/pasta/$', views.pasta, name='pasta'),
	url(r'cooking/fried/$', views.fried, name='fried'),
	url(r'cooking/desserts/$', views.desserts, name='desserts'),
]
