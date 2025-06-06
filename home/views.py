from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import DailyMealPlan
from django.http import JsonResponse
from django.utils import timezone
# Create your views here.
from datetime import date

def index(request):
    return render(request,"home/index.html")


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Change to your desired redirect page
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login_view')  # Change to your desired redirect URL name

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=name).exists():
            messages.error(request, 'An account with this email already exists.')
        else:
            user = User.objects.create_user(username=name, email=email, password=password, first_name=name)
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('home')  # Change to your app's dashboard route

    return render(request, 'login/login.html')  # Use 'login.html' if both forms are on same page

def meal(request):
    return render(request,"home/meal.html")

@login_required
def meal_plan_view(request):
    selected_date = request.GET.get('date')

    if not selected_date:
        selected_date = date.today()  # default to today
    meal, created = DailyMealPlan.objects.get_or_create(user=request.user, date=selected_date)

    if request.method == 'POST':
        meal.breakfast = request.POST.get('breakfast', '')
        meal.lunch = request.POST.get('lunch', '')
        meal.snacks = request.POST.get('snacks', '')
        meal.dinner = request.POST.get('dinner', '')
        meal.save()
        return redirect('meal_planner')

    return render(request, 'home/meal.html', {'meal': meal, 'selected_date': selected_date})

def spoonacular(request):
    return render(request,'home/spoonacular.html')

def blog(request):
    return render(request,"home/blog.html")