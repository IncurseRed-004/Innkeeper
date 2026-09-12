from django.shortcuts import render, redirect

from InnKeeper_app.form import Customer_Form
from InnKeeper_app.models import Customer


def customer_dashboard(request):
    return render(request,"customer/customer_base.html")

def customer_profile(request):
    user_data = request.user
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