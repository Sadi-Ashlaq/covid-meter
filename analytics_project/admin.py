from django.contrib import admin
from .models import Country

from import_export.admin import ImportExportModelAdmin

# Register your models here.

# admin.site.register(Country)

@admin.register(Country)

class ViewAdmin(ImportExportModelAdmin):
    list_display = ('Country', 'Total_Cases', 'New_Cases', 'Total_Deaths' , "New_Deaths")
