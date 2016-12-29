from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	context = {}
	return render(request, 'home/index.html', context)

def archery(request):
	context = {}
	return render(request, 'home/archery.html', context)

def cooking(request):
	context = {}
	return render(request, 'home/cooking.html', context)

def poker(request):
	context = {}
	return render(request, 'home/poker.html', context)

def projects(request):
	context = {}
	return render(request, 'home/projects.html', context)
