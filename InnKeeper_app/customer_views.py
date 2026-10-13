from django.shortcuts import render, redirect

from InnKeeper_app.form import Customer_Form, Chat_form
from InnKeeper_app.models import Customer, Resorts, Booking, Facilities, Schedules, Chat


def customer_dashboard(request):
    return render(request,"customer/customer_base.html")

def customer_profile(request):
    user_data = request.user
    print(user_data.id)
    customer_data =Customer.objects.get(user = user_data)
    # print(customer_data.id)
    # print(customer_data.name)
    # print(customer_data.phone)
    # print(customer_data.email)
    # print(customer_data.address)
    return render(request,"customer/customer_profile.html",{"customer_data":customer_data})

def edit_customer(request,id):
    data = Customer.objects.get(id =id)
    if request.method == "POST":
        form = Customer_Form(request.POST, instance=data)
        if  form.is_valid():
            form.save()
            return redirect('customer_profile')
    else:
        form = Customer_Form(instance = data)
    return render(request,'customer/edit_customer.html',{"form":form})




def view_details(request,facility_id):
    details = Facilities.objects.get(id=facility_id)

    if request.user.is_authenticated:
        return render(request,"resort_details.html",{"details":details})
    else:
        return redirect("Login")

def book_now(request,id):
    slots = Schedules.objects.filter(facilities=id)
    print(slots)
    return render(request,"book_now.html",{"slots":slots})

def select_slot(request,id):

    print("Logged in user:", request.user)
    print("User ID:", request.user.id)


    customer_var = Customer.objects.get(user = request.user)
    slot_var = Schedules.objects.get(id=id)

    if request.method =="POST":

        # Booking.objects.create( customer = customer_var,schedule = slot_var) # customer and  schedule here come from the Booking model
        booking = Booking()
        booking.customer=customer_var
        booking.schedule=slot_var
        booking.save()
        slot_var.schedule_status = 1
        slot_var.save()
        return redirect("booking_success")


    return render(request,"select_slot.html",{"customer":customer_var,"slot":slot_var})


def booking_success(request):
    return render(request,"booking_success.html")



def booking_history(request):
    customer = Customer.objects.get(user = request.user)
    history = Booking.objects.filter(customer = customer)
    print(history)
    return render(request,"customer/booking_history.html",{"history":history})


def chat_with(request,id):
    booking = Resorts.objects.get(id = id)
    print(booking)
    customer = Customer.objects.get(user = request.user)
    print(customer)
    # resort = booking.schedule.facilities.resort
    # print(resort)

    if request.method =="POST":
        chat = Chat()
        chat.customer = customer
        chat.resort=booking
        chat.message = request.POST.get("message")
        chat.save()
        return redirect("booking_history")


    return render(request,"customer/chat.html",{"booking":booking,"customer":customer})



