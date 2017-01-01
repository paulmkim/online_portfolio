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

def highlights(request):
	context = {}
	return render(request, 'home/foodCategories/highlights.html', context)
def breakfast(request):
	context = {}
	return render(request, 'home/foodCategories/breakfast.html', context)
def stock(request):
	context = {}
	return render(request, 'home/foodCategories/stock.html', context)
def fastCooking(request):
	context = {}
	return render(request, 'home/foodCategories/fastCooking.html', context)
def salads(request):
	context = {}
	return render(request, 'home/foodCategories/salads.html', context)
def groundMeat(request):
	context = {}
	return render(request, 'home/foodCategories/groundMeat.html', context)
def roasts(request):
	context = {}
	return render(request, 'home/foodCategories/roasts.html', context)
def pasta(request):
	context = {}
	return render(request, 'home/foodCategories/pasta.html', context)
def fried(request):
	context = {}
	return render(request, 'home/foodCategories/fried.html', context)
def desserts(request):
	context = {}
	return render(request, 'home/foodCategories/desserts.html', context)
