from typing import Optional
from django.shortcuts import render
from products.models import products
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.

class myLoginView(LoginView):
    def form_valid(self,form):
        messages.success(self.request,'Logged in succesfully!!')
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,'Invalid Credentials!!!!')
        return super().form_invalid(form)

class myLogOutview(LogoutView):
    def get_next_page(self):
        messages.success(self.request,"You Logout Successfully!!")
        return reverse_lazy('login_page')
        
