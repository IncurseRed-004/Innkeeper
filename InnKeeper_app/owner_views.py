from django.shortcuts import render, redirect

from InnKeeper_app.form import Customer_Form, Owner_Form, ResortForm, Facility_Form
from InnKeeper_app.models import Customer, Owner, Resorts, Facilities


def owner_dashboard(request):
    return render(request,"owner/owner_base.html")

def owner_profile(request):
    user_data = request.user #currently logged in user
    print(user_data.id)
    owner_data =Owner.objects.get(user = user_data) #owner connected to the currently logged in Login
    # print("id: ",owner_data.id)
    # print("name: ",owner_data.name)
    # print("phone: ",owner_data.phone)
    # print("email: ",owner_data.email)
    return render(request,"owner/owner_profile.html",{'owner_data':owner_data})

def edit_owner(request, id):
    data = Owner.objects.get(id=id)
    if request.method == 'POST':
        form = Owner_Form(request.POST, instance=data) #instance = data -Create the form using this existing resort's data
        if form.is_valid():
            form.save()
            return redirect('owner_profile')
    else:
        form = Owner_Form(instance=data)
    return render(request, 'owner/edit_owner.html', {'form': form})


# add resort

def resort_add(request):

        data = Owner.objects.get(user = request.user)

        if request.method == 'POST':
            form = ResortForm(request.POST, request.FILES)

            if form.is_valid():
                resort = form.save(commit=False)
                resort.owner = data
                resort.save()

                return redirect('resort_facilities', resort_id=resort.id)
        else:
            form = ResortForm()
        return render(request, 'owner/resort_add.html', {'form':form})



# add facilities

def resort_facility(request,resort_id):
    data = Resorts.objects.get(id=resort_id)

    if request.method == 'POST':
        form = Facility_Form(request.POST) # no instance used here - because we create new form

        if form.is_valid():
            facilities =  form.save(commit=False)
            facilities.resort = data
            facilities.save()

        return redirect('owner_dashboard')
    else:
        form = Facility_Form()

    return render(request, 'owner/resort_facility.html', {'form':form})


# edit resort detailes

def edit_resort(request, id):
    owner = Owner.objects.get(user=request.user)
    resort = Resorts.objects.get(id=id, owner=owner)

    if request.method == 'POST':
        form = ResortForm(request.POST,request.FILES,instance=resort)

        if form.is_valid():
            form.save()
            return redirect('my_resorts')
    else:
        form = ResortForm(instance=resort)

    return render(request,'owner/edit_resort.html',{'form': form,'resort': resort})


# edit facilities

def edit_facilities(request,resort_id):
    resort = Resorts.objects.get(id=resort_id)
    data = Facilities.objects.get(resort=resort)

    if request.method =="POST":
        form = Facility_Form(request.POST,instance=data)

        if form.is_valid():
            form.save()
        return redirect('my_resorts')

    else:
        form =Facility_Form(instance=data)

    return render(request,'owner/edit_facilities.html',{'form':form})


def my_resorts(request):
    resorts = Resorts.objects.all()
    return render(request,'owner/my_resorts.html',{'resorts':resorts})