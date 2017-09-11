from django.contrib import admin

#for import export package
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Project


admin.site.register(Project)
