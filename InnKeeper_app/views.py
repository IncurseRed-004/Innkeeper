from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


from InnKeeper_app.form import Login_form, Customer_Form, Owner_Form
from InnKeeper_app.models import Resorts, Facilities, Schedules, Customer, Booking


# Create your views here.

def landing_page(request):
    return render(request, 'Landing.html')

def dashboard(request):
    return render(request, 'Dashboard.html')

def Logout_view(request):
    logout(request)
    return redirect("Login")


def account_dashboard(request):

    user = request.user
    if user is not None:
        login(request, user)

        if user.is_customer:
            return redirect('customer_dashboard')

        elif user.is_owner:
            return redirect('owner_dashboard')

        elif user.is_staff:
            return redirect('admin_dashboard')
    else:
        print("Invalid Credentials")


def Login(request):

    if request.method=="POST":

        username =request.POST.get('uname')
        password =request.POST.get("pass")

        user= authenticate(username = username,password = password)

        if user is not None:
            login(request, user)

            if user.is_customer:
                return redirect('customer_dashboard')

            elif user.is_owner:
                return redirect('owner_dashboard')

            elif user.is_staff:
                return redirect('admin_dashboard')

        else:
            print("Invalid Credentials")
            # messages.info(request,"Invalid Credentials :(")
    return render(request, 'Login.html')

def customer_registration(request):
    login_data = Login_form()
    data = Customer_Form()

    if request.method =="POST":
        # receive data from frontend
        login_data = Login_form(request.POST)
        data = Customer_Form(request.POST)

        if login_data.is_valid() and data.is_valid():
            cust = login_data.save(commit=False)
            cust.is_customer = True
            cust.save()
            x = data.save(commit=False)
            x.user =cust
            x.save()
            return redirect("Login")


    return render(request,'customer_page.html',{'data_key':data,'login_data':login_data})

def owner_registration(request):
    login_data = Login_form()
    data = Owner_Form()

    if request.method =='POST':
        #receive data from frontend
        login_data = Login_form(request.POST)
        data = Owner_Form(request.POST)

        if login_data.is_valid() and data.is_valid():
            owner = login_data.save(commit=False)
            owner.is_owner = True
            owner.save()

            y =data.save(commit=False)
            y.user =owner
            y.save()

            return redirect("Login")
    return render(request,'owner_page.html',{'data_key':data,'login_data':login_data})

# list resort

def list_resorts(request):
    facility = Facilities.objects.all()
    # print(facility)
    return render(request,"Landing.html",{"facility":facility})

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
        return redirect("booking_success")


    return render(request,"select_slot.html",{"customer":customer_var,"slot":slot_var})


def booking_success(request):
    return render(request,"booking_success.html")


def base_landing(request):
    return render(request,"base_landing.html")