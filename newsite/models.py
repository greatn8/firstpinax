from django.db import models

# Create your models here.
from django.db import models
from location_field.models.plain import PlainLocationField

class Project(models.Model):
	#camewutg maps package
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)

   
    Project_ID = models.IntegerField(blank=False, primary_key=True)
    Project_Title = models.CharField(max_length=120, blank=False, null=True)
    Project_Type = models.CharField(max_length=120, blank=False, null=True)
    Project_Post = models.CharField(max_length=120, blank=False, null=True)
    Project_Suburb = models.CharField(max_length=120, blank=False, null=True)    
    Project_State = models.CharField(max_length=120, blank=False, null=True)
    Project_Stage = models.CharField(max_length=120, blank=False, null=True)
    Project_Category = models.CharField(max_length=120, blank=False, null=True)
    PROJ_STATUST_DESC = models.CharField(max_length=200, blank=False, null=True)
    PROJ_START_DATE_DETAIL = models.DateField(auto_now_add=False)
    PROJ_END_DATE_DETAIL = models.DateField(auto_now_add=False)
    PROJ_VALUE = models.IntegerField(blank=False, null=True)
    PROJ_VALUE_DESC = models.CharField(max_length=120, blank=False, null=True)
    PROJ_DETAIL_TEXT = models.CharField(max_length=1000, blank=False, null=True)

#class Business(models.Model):
#	Business_Name = models.CharField(max_length=120, blank=False, null=True)
#	Business_Name_Status = models.CharField(max_length=120, blank=False, null=True)
#	Date_Of_Registration = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
#	Date_Of_Cancellation = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
#	Renewal_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
#	Former_State_Number = models.CharField(max_length=120, blank=True, null=True)
#	Previous_State_Of_Registration = models.CharField(max_length=120, blank=True, null=True)
#	ABN = models.CharField(max_length=120, blank=True, null=True)

