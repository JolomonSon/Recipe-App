from django.urls import path
from account import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile')
]