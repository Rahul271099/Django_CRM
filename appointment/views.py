from django.shortcuts import render,redirect
from .models import appointment
from .forms import AppointmentForm
from django.contrib import messages
from django.http import Http404

# Create your views here.
def appointment_list(request):
    query = appointment.objects.filter(enterd_by = request.user)
    flag = query.exists() 
    data = {'apt_d':query,'flag':flag}
    return render(request,'appointment/appointments.html',data)


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.enterd_by = request.user
            doctor.save()
            messages.success(request,"Your appointment sheduled successfully")
            return redirect('appointment_list')  # Redirect to doctor detail page
    else:
        form = AppointmentForm()
    return render(request, 'appointment/addAppointment.html', {'aform': form})
