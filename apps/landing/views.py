from django.shortcuts import render

def index(request):
    """header"""
    return render(request, 'landing/template/base.html')