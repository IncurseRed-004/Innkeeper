from django.contrib import admin

from InnKeeper_app.models import Login, Customer, Owner, Resorts, Facilities, Schedules, Student

# Register your models here.

admin.site.register(Login)
admin.site.register(Customer)
admin.site.register(Owner)
admin.site.register(Resorts)
admin.site.register(Facilities)
admin.site.register(Schedules)
admin.site.register(Student)