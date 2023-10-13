from django.shortcuts import render,redirect
from appointment.models import appointment
from products.models import products
from doctor.models import doctor_details
from deals.models import deals
from django.contrib.auth.models import User
from django.db.models import Count,Sum
from .forms import RegistrationForm,UpdateEmployeeForm
from django.contrib import messages

# Create your views here.
def user(request):
    return render(request,"admin_module/adminDashboard.html")

def appointments_view(request):
    # a_data = appointment.objects.all()
    user_data = User.objects.all()
    user_count = []
    
    for user in user_data:
        count = appointment.objects.filter(enterd_by = user.id).count()
        if count > 0:
            user_count.append((user.username,count))
    context = {
        'count':user_count
    }
    return render(request,"admin_module/adminappointments.html",context)

def employee_data_view(request):
    emp_data = User.objects.all()
    context2 = {
        'emp_data':emp_data
    }
    return render(request,"admin_module/employeedetail.html",context2)

def register(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request,'admin_module/register.html',{'form_data':form})
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request,'Account Created Successfully for'+" "+ user_name)
            return redirect(employee_data_view)
        else:
            messages.error(request,"Please Check your form there is some issues in form")
            return render(request,'base/register.html',{'form_data':form})
        
    return render(request,'base/register.html',{'form_data':form})

def updateEmployee(request,id):
    if request.method == "POST":
        e_data = User.objects.get(pk=id)
        form = UpdateEmployeeForm(request.POST,instance=e_data)
        if form.is_valid():
            form.save()
            messages.success(request,"User Updated successfully")
        return redirect("employee")
    else:
        e_data = User.objects.get(pk=id)
        form = UpdateEmployeeForm(instance=e_data)
    context = {
        'form_data':form
    }
    return render(request,'admin_module/updateEmployee.html',context)

def deals_view(request):
    a_data = User.objects.all()
    count_deals = []

    for user in a_data:
        count = deals.objects.filter(entered_by = user.id).count()
        if count > 0:
            count_deals.append((user.username,count))
    context = {
        'deal_count':count_deals
    }
    return render(request,"admin_module/admindeals.html",context)