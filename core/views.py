from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
def login_view(request):
    return render(request, 'core/login.html')
@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')
