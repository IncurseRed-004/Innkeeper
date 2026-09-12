from django.shortcuts import render, redirect

from InnKeeper_app.form import Owner_Form
from InnKeeper_app.models import Customer, Owner


def admin_dashboard(request):
    return render(request,'admin/admin_base.html')


#customer table
def view_customer(request):
    data = Customer.objects.all()
    return render(request,'admin/view_customer.html',{'data':data})

def delete_customer(request,id):
    data = Customer.objects.get(id=id)
    data.delete()
    return redirect('admin/view_customer.html')

#owner table
def view_owner(request):
    data = Owner.objects.all()
    return render(request,'admin/view_owner.html',{'data':data})

def delete_owner(request,id):
    data = Owner.objects.get(id=id)
    data.delete()
    return redirect('admin/view_owner.html')

# def update_owner(request,id):
#     data = Owner.objects.get(id=id)
#     if request.method == 'POST':
#         form = Owner_Form(request.POST, instance=data)
#
#         if form.is_valid():
#             form.save()
#             return redirect('admin/view_customer.html')
#     return render(request,'admin/update_owner.html',{'form':form})

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