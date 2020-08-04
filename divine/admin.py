from django.contrib import admin

from .models import Appointment
# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Date', 'PhoneNo')
    search_fields = ('Name', 'Date')


admin.site.register(Appointment, AppointmentAdmin)
