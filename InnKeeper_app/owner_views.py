from django.shortcuts import render, redirect

from InnKeeper_app.form import Customer_Form, Owner_Form
from InnKeeper_app.models import Customer, Owner


def owner_dashboard(request):
    return render(request,"owner/owner_base.html")

def owner_profile(request):
    user_data = request.user
    print(user_data.id)
    owner_data =Owner.objects.get(user = user_data)
    # print("id: ",owner_data.id)
    # print("name: ",owner_data.name)
    # print("phone: ",owner_data.phone)
    # print("email: ",owner_data.email)
    return render(request,"owner/owner_profile.html",{'owner_data':owner_data})

def edit_owner(request, id):
    data = Owner.objects.get(id=id)
    if request.method == 'POST':
        form = Owner_Form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('owner_profile')
    else:
        form = Owner_Form(instance=data)
    return render(request, 'owner/edit_owner.html', {'form': form})