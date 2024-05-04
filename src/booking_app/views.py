from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def rules(request):
    return render(request, 'rules.html')

def establishments(request):
    return render(request, 'establishments.html')

