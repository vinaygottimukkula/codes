from django.contrib import admin

# Register your models here.
from .models import student
admin.site.register(student)
admin.site.register(roolnumber)
admin.site.register(dateofbirth)