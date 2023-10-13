"""
URL configuration for medicalapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import myLoginView
from .views import new_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myLoginView.as_view(template_name = 'base/login.html'),name='login_page'),
    path('dashboard/',new_page,name='dashboard'),
    path('account/',include('accounts.urls'),name="account"),
    path('products/',include('products.urls'),name="products"),
    path('doctors/',include('doctor.urls'),name="doctors"),
    path('appointment/',include('appointment.urls'),name="appointment"),
    path('deals/',include('deals.urls'),name="deals"),
    path('Cadmin/',include('admin_module.urls'),name="admin_user"),
]
if settings:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)