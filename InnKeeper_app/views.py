from django import forms
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect


from InnKeeper_app.form import Login_form, Customer_Form, Owner_Form


# Create your views here.

def landing_page(request):
    return render(request, 'Landing.html')

def dashboard(request):
    return render(request, 'Dashboard.html')

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