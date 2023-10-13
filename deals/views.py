from django.shortcuts import render,redirect
from .models import deals
from .forms import DealsForm
from django.contrib import messages
from django.http import Http404
# Create your views here.

def deals_list(request):
    query = deals.objects.filter(entered_by = request.user)
    flag = query.exists() 
    data = {'deal_d':query,'flag':flag}
    return render(request,'deals/deals.html',data)


def create_deals(request):
    if request.method == 'POST':
        form = DealsForm(request.POST)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.entered_by = request.user
            deal.save()
            messages.success(request,"Your deal added Successfully")
            return redirect('deals_list')  # Redirect to doctor detail page
    else:
        form = DealsForm()
    return render(request, 'deals/adddeal.html', {'dform': form})
