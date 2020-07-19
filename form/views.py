from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request, 'form/index.html')
    #return HttpResponse('Hello World')

# Create your views here.
