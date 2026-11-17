from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from InnKeeper_app.form import Owner_Form
from InnKeeper_app.models import Customer, Owner, Facilities

@login_required(login_url = 'Login')
def admin_dashboard(request):
    return render(request,'admin/admin_base.html')


#customer table
@login_required(login_url = 'Login')
def view_customer(request):
    data = Customer.objects.all()
    return render(request,'admin/view_customer.html',{'data':data})

@login_required(login_url = 'Login')
def delete_customer(request,id):
    data = Customer.objects.get(id=id)
    data.delete()
    return redirect('admin/view_customer.html')

#owner table
@login_required(login_url = 'Login')
def view_owner(request):
    data = Owner.objects.all()
    return render(request,'admin/view_owner.html',{'data':data})

@login_required(login_url = 'Login')
def delete_owner(request,id):
    data = Owner.objects.get(id=id)
    data.delete()
    return redirect('view_owner')

# def update_owner(request,id):
#     data = Owner.objects.get(id=id)
#     if request.method == 'POST':
#         form = Owner_Form(request.POST, instance=data)
#
#         if form.is_valid():
#             form.save()
#             return redirect('admin/view_customer.html')
#     return render(request,'admin/update_owner.html',{'form':form})

@login_required(login_url = 'Login')
def update_owner(request, id):
    data = Owner.objects.get(id=id)
    if request.method == 'POST':
        form = Owner_Form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_owner')
    else:
        form = Owner_Form(instance=data)
    return render(request, 'admin/update_owner.html', {'form': form})


@login_required(login_url = 'Login')
def view_resorts(request):
    data = Facilities.objects.all()
    print(data)
    return render(request,'admin/view_resorts.html',{'data':data})