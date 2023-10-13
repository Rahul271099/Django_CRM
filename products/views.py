from django.shortcuts import render,redirect
from .models import products
from .forms import ProductForm
from django.http import HttpResponse
from django.contrib import messages


# Read data view
def products_list(request):
    if request.user.is_authenticated:
        products_data = products.objects.all()
        data = {'pro_d':products_data}
        return render(request,'products/list.html',data)
    else:
        return redirect('login_page')

# create view
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.enterd_by = request.user
            product_price = form.cleaned_data['product_price']
            if product_price < 0:
                messages.error(request, "Product price cannot be negative. Please enter a valid price.")
                return render(request, 'products/addProduct.html', {'pform': form})
            data.save()
            messages.success(request,"Product added successfully")
            return redirect('products_list')
        else:
            return HttpResponse("error")
    else:
        form = ProductForm()
    return render(request, 'products/addProduct.html', {'pform': form})      

# upadte view
def update_Product(request,id):
    if request.method == "POST":
        P_data = products.objects.get(pk=id)
        form = ProductForm(request.POST,instance=P_data)
        if form.is_valid():
            product_price = form.cleaned_data['product_price']
            if product_price < 0:
                messages.error(request, "Product price cannot be negative. Please enter a valid price.")
                return render(request, 'products/addProduct.html', {'pform': form})
            form.save()
            messages.success(request,"Product Updated successfully")
        return redirect("products_list")
    else:
        P_data = products.objects.get(pk=id)
        form = ProductForm(instance=P_data)
    context = {
        'form':form
    }
    return render(request,'products/updateProduct.html',context)
    
# delete view
def delete_Product(request,id):
    p_data = products.objects.get(pk=id)
    p_data.delete()
    messages.success(request,"Product Deleted Successfully")
    return redirect("products_list")