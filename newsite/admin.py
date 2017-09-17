from django.contrib import admin

#for import export package
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from newsite.models import Project

#for dhango-import-export
from import_export import resources

class ProjectResource(resources.ModelResource):

    class Meta:
        model = Project
        exclude = ('Project_Category','location',)
        import_id_fields = ['Project_ID']

class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource        

#register admin
admin.site.register(Project, ProjectAdmin)


