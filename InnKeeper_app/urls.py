from django.contrib import admin
from django.urls import path

from InnKeeper_app import views, admin_views, customer_views, owner_views

urlpatterns = [
    path('landing_page',views.landing_page,name='landing_page'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('Login',views.Login,name='Login'),
    path("customer_registration",views.customer_registration,name="customer_registration"),
    path("owner_registration",views.owner_registration,name="owner_registration"),

    #admin_views
    path("admin_dashboard",admin_views.admin_dashboard,name="admin_dashboard"),
    path('view_customer',admin_views.view_customer,name="view_customer"),
    path('delete_customer/<int:id>',admin_views.delete_customer,name="delete_customer"),
    path('view_owner',admin_views.view_owner,name="view_owner"),
    path('delete_owner/<int:id>',admin_views.delete_owner,name="delete_owner"),
    path("update_owner/<int:id>",admin_views.update_owner,name="update_owner"),

    #customer_views
    path("customer_dashboard",customer_views.customer_dashboard,name="customer_dashboard"),
    path('customer_profile',customer_views.customer_profile,name="customer_profile"),
    path('edit_customer/<int:id>',customer_views.edit_customer,name="edit_customer"),


    #owner_views
    path("owner_dashboard",owner_views.owner_dashboard,name="owner_dashboard"),
    path('owner_profile',owner_views.owner_profile,name="owner_profile"),
    path("edit_owner/<int:id>",owner_views.edit_owner,name="edit_owner"),
    path('resort_add',owner_views.resort_add,name="resort_add"),
    path('resort_facility/<int:resort_id>/',owner_views.resort_facility,name='resort_facilities'),
    path('edit_resort/<int:id>/',owner_views.edit_resort,name='edit_resort'),
    path('edit_facilities/<int:resort_id>/',owner_views.edit_facilities,name='edit_facilities'),
    path('my_resorts/',owner_views.my_resorts,name='my_resorts'),

]