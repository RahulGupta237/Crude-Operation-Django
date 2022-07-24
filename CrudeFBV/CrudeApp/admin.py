from csv import list_dialects
from django.contrib import admin 
from CrudeApp.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','email','role')
