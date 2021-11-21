from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# When ever we get request to /product URL then call -> index function


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'product': products})


def new(request):
    return HttpResponse('New Products')





