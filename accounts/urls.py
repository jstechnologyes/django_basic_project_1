from django.urls import path
from .import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('lgoin', views.login, name='login'),
    path('logout', views.logout, name='logout'),

]
