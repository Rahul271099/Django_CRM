from django.shortcuts import render,redirect
from .models import doctor_details
from .forms import DoctorForm
from django.contrib import messages

# Create your views here.
def doctor_list(request):
    products_data = doctor_details.objects.all()
    data = {'doct_d':products_data}
    return render(request,'doctor/doctorTable.html',data)


def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.enter_by = request.user
            dnumber = form.cleaned_data['dnumber']
            if len(dnumber) < 10:
                messages.error(request, "Please enter a valid mobile number.")
                return render(request, 'doctor/addDoctor.html', {'dform': form})
            doctor.save()
            messages.success(request,"Doctor added successfully")
            return redirect('doctors_list')  # Redirect to doctor detail page
    else:
        form = DoctorForm()
    return render(request, 'doctor/addDoctor.html', {'dform': form})

# update view
def Update_doctor(request,id):
    if request.method == "POST":
        d_data = doctor_details.objects.get(pk=id)
        form = DoctorForm(request.POST,instance = d_data)
        if form.is_valid():
            dnumber = form.cleaned_data['dnumber']
            if len(dnumber) < 10:
                messages.error(request, "Product price cannot be negative. Please enter a valid price.")
                return render(request, 'doctor/updateDoctor.html', {'dform': form})
            form.save()
            messages.success(request,"Doctor Data Updated Successfully")
        return redirect("doctors_list")
    else:
        d_data = doctor_details.objects.get(pk=id)
        form = DoctorForm(instance = d_data)
    context ={
        'form':form
    }
    return render(request,"doctor/updateDoctor.html",context)


# delete view

def Delete_doctor(request,id):
    d_data = doctor_details.objects.get(pk=id)
    d_data.delete()
    messages.success(request,"Doctor details Deleted Successfully")
    return redirect("doctors_list")