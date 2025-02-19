from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

def user_page(request):
    return HttpResponse("Hello, world. You're at the user page.")

def specific_user(request, user_id):
    return HttpResponse(f"User ID: {user_id}")

def login_page(request):
    return HttpResponse("Login Page")

def logout_page(request):
    return HttpResponse("Logout Page")

def register_page(request):
    return HttpResponse("Register Page")

def user_dashboard(request):
    return render(request, 'users/user_dashboard.html')

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'users/user_profile.html', {'user': user})
