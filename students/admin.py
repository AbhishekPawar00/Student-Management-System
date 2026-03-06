from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','phone','course','date_of_admission')
    search_fields = ('full_name','course')
    list_filter = ('course','date_of_admission')
admin.site.register(Student, StudentAdmin)