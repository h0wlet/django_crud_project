from django.contrib import admin
from .models import Student, University


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth', 'institution', 'year')


admin.site.register(Student, StudentAdmin)


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'short_name',  'date')


admin.site.register(University, UniversityAdmin)

