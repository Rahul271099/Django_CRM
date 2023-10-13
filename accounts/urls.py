from django.urls import path
from .views import myLoginView,myLogOutview

urlpatterns = [
    path('login/',myLoginView.as_view(template_name = 'base/login.html'),name='login_page'),
    path('logout/',myLogOutview.as_view(),name='logout_page'),
]