from django.urls import path,include
from .import views



urlpatterns = [
    path('',views.home_view,name='home'),
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact_view,name='contact'),
    path('booking/',views.booking_view,name='booking'),
    path('department/',views.department_view,name='department'),
    path('doctors/',views.doctors_view,name='doctors'),
    
]