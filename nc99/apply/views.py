from django.shortcuts import render

def index(request):
    return render(request, 'apply/index.html', {})

def create(request):
    return render(request, 'apply/create.html', {})
