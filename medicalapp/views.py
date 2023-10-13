from django.shortcuts import render,redirect
from products.models import products
from doctor.models import doctor_details
from appointment.models import appointment
from deals.models import deals

def new_page(request):
    appointments = appointment.objects.filter(enterd_by = request.user)
    deal_data = deals.objects.filter(entered_by = request.user)
    count = products.objects.count()
    count2 = doctor_details.objects.count()
    count3 = appointments.count()
    count4 = deal_data.count()

    if request.user.is_superuser:
        count3 = appointment.objects.count()
        count4 = deals.objects.count()

    context = {
        'count':count,
        'count2':count2,
        'count3':count3,
        'count4':count4,
    }
    return render(request,'base/index.html',context)