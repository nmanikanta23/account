from django.urls import path
from . import views  # Import all views from this app

urlpatterns = [
    path('register/', views.register_page, name='register'),  # Registration page
    path('login/', views.login_page, name='login'),          # Login page
    path('logout/', views.logout_user, name='logout'),       # Logout action
    path('', views.home_page, name='home'),                  # Home page
]
