from django.contrib import admin
from .models import appointment

class customAppointment(admin.ModelAdmin):
    list_display = ['doct_name','schedule_date','Schedule_time','enterd_by']



# Register your models here.
admin.site.register(appointment,customAppointment)
admin.site.site_header = 'Admin Panel'
admin.site.site_title = 'Admin'
admin.site.index_title = 'medical app Administrator'