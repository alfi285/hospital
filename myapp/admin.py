from django.contrib import admin
from .models import Departments,Doctors,Booking


admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name', 'p_phone', 'p_email', 'doc_name',)
admin.site.register(Booking)

# Register your models here.

