from django.contrib import admin
from django.urls import path

from InnKeeper_app import views

urlpatterns = [
    path('landing_page',views.landing_page,name='landing_page'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('login',views.login,name='login'),
]