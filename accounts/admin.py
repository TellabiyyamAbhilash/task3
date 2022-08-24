from django.contrib import admin

# Register your models here.
from accounts.models import User,Doctor,Patient,Category,Blog,Appointment

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Appointment)
