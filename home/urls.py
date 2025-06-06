from django.urls import path
from .views import index, login_view, logout_view, signup_view, meal_plan_view, spoonacular, blog
urlpatterns = [
    path('',index,name='home'),
    path('login/',login_view, name='login_view'),
    path('logout/',logout_view,name='logout'),
    path('signup/', signup_view, name='signup'),
    path('spoonacular/',spoonacular,name="spoonacular"),
    path('meal-planner/', meal_plan_view, name='meal_planner'),
    path('blog/',blog,name="blog")
]
