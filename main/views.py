from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def dashboard(request):
    return render(request, 'main/dashboard.html')