from django.contrib import admin
from django.urls import path

from InnKeeper_app import views, admin_views, customer_views, owner_views

urlpatterns = [
    path('',views.list_resorts,name='list_resorts'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('Login',views.Login,name='Login'),
    path("Logout_view",views.Logout_view,name="Logout_view"),
    path("customer_registration",views.customer_registration,name="customer_registration"),
    path("owner_registration",views.owner_registration,name="owner_registration"),
    path('account_dashboard',views.account_dashboard,name='account_dashboard'),

    path("view_details/<int:facility_id>",views.view_details,name="view_details"),
    path('book_now/<int:id>',views.book_now,name="book_now"),
    path('select_slot/<int:id>',views.select_slot,name='select_slot'),
    path("booking_success",views.booking_success,name="booking_success"),
    path('base_landing',views.base_landing,name='base_landing'),

    #admin_views
    path("admin_dashboard",admin_views.admin_dashboard,name="admin_dashboard"),
    path('view_customer',admin_views.view_customer,name="view_customer"),
    path('delete_customer/<int:id>',admin_views.delete_customer,name="delete_customer"),
    path('view_owner',admin_views.view_owner,name="view_owner"),
    path('delete_owner/<int:id>',admin_views.delete_owner,name="delete_owner"),
    path("update_owner/<int:id>",admin_views.update_owner,name="update_owner"),
    path('view_resorts',admin_views.view_resorts,name="view_resorts"),

    #customer_views
    path("customer_dashboard",customer_views.customer_dashboard,name="customer_dashboard"),
    path('customer_profile',customer_views.customer_profile,name="customer_profile"),
    path('edit_customer/<int:id>',customer_views.edit_customer,name="edit_customer"),
    path('booking_history',customer_views.booking_history,name="booking_history"),


    #owner_views
    path("owner_dashboard",owner_views.owner_dashboard,name="owner_dashboard"),
    path('owner_profile',owner_views.owner_profile,name="owner_profile"),
    path("edit_owner/<int:id>",owner_views.edit_owner,name="edit_owner"),
    path('resort_add',owner_views.resort_add,name="resort_add"),
    path('resort_facility/<int:resort_id>/',owner_views.resort_facility,name='resort_facilities'),
    path('edit_resort/<int:id>/',owner_views.edit_resort,name='edit_resort'),
    path('edit_facilities/<int:resort_id>/',owner_views.edit_facilities,name='edit_facilities'),
    path('delete_resort/<int:resort_id>/',owner_views.delete_resort,name='delete_resort'),
    path('my_resorts/',owner_views.my_resorts,name='my_resorts'),
    path('add_schedules/<int:id>/',owner_views.add_schedules,name='add_schedules'),
    path('view_schedules/<int:id>',owner_views.view_schedules,name='view_schedules'),
    path('delete_schedule/<int:id>',owner_views.delete_schedule,name='delete_schedule'),
    path('booking_status',owner_views.booking_status,name='booking_status'),
    path('approved/<int:id>',owner_views.approved,name='approved'),
    path('rejected/<int:id>',owner_views.rejected,name='rejected'),
]