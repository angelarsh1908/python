from django.contrib import admin
from .models import*

admin.site.register(user)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)

# Register your models here.
