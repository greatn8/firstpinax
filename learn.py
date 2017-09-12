# -*- coding: utf-8 -*-
#! /usr/bin/env python

#this fixed app not installed error?!
import os,sys
def setup_environment():
 pathname = os.path.dirname(sys.argv[0])
 sys.path.append(os.path.abspath(pathname))
 sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
 os.environ['DJANGO_SETTINGS_MODULE'] = 'newsite.settings'

setup_environment()

import django
django.setup()
###

from django.shortcuts import render
from django.http import HttpResponse
import urllib2
from bs4 import BeautifulSoup
##########3line that is breadking 
from newsite.models import Project
#for splitting strings
import re


#for django-location-field
from location_field.models.plain import PlainLocationField

#added for get function
import requests

def token():
	global finaltoken
	url = "http://cordellprojectsapi.cordell.com.au/api/Projects/InvokeAPI"

	headers = {
    	'username': "c-130769",
    	'password': "vnN#QNth$DRxWSq3q8f#",
    	
    	}

	responsetoken = requests.request("POST", url, headers=headers)

	tokenraw = (responsetoken.text)
	print "Token Raw Response:",tokenraw
	print "Type of Raw response",type(tokenraw)
	tokenrawstring = str(tokenraw)
	print tokenrawstring
	print type(tokenrawstring)
	
	#gets info between </token> tag inside tokenstringraw
	result = re.search('<TOKEN>(.*)</TOKEN>', tokenrawstring)
	#final token in string format 
	finaltoken = result.group(1)
	#print for testing
	print type(finaltoken), finaltoken
 
#calling token function to get token
token()	

##example project search date inout manually grabs token from token()
def getprojectsdate():	
	url = "http://cordellprojectsapi.cordell.com.au/api/Projects/ProjectGetAllData"

	querystring = {"FROMDATE":"10/08/2017","TODATE":"11/08/2017"}

	headers = {
    	'token': finaltoken,
    
  
    }

	response = requests.request("POST", url, headers=headers, params=querystring)

	resultraw = (response.text)
	print "Result Raw Response:",resultraw
	print "Type Result Raw response",type(resultraw)
	resultrawstring = str(resultraw)
	print resultrawstring
	print type(resultrawstring)

	#makine string into soup and speicify its xml
	souprawresult = BeautifulSoup(resultrawstring, 'xml')
	
	#print type of souop
	print "soup type",type(souprawresult)

	#gets just project names
	projectnames = souprawresult.find_all('PROJ_TITLE')
	print projectnames
	print type(projectnames)

#	gets just the text without tags
#	for proj in projectnames:
#	print proj.text

	#gets all projects in soup
	projectz = souprawresult.find_all('PROJECT')
	print projectz
	print type(projectz)
	
	for pro in projectz:

		city = pro.PROJ_ADDRESS1.string
		print pro.PROJ_ADDRESS1
		print "type",type(city)

		projectid = pro.PROJ_PROJECT_ID.string
		print pro.PROJ_PROJECT_ID
		
		projecttitle = pro.PROJ_TITLE.string
		print pro.PROJ_TITLE
		
		projectcipher = pro.PROJ_CAT1_TYPE_DESC.string
		print pro.PROJ_CAT1_TYPE_DESC

		projectpost = pro.PROJ_POSTCODE.string
		print pro.PROJ_POSTCODE
		
		projectsub = pro.PROJ_SUBURB.string
		print pro.PROJ_SUBURB

		projectstate = pro.PROJ_STATE_CODE.string
		print pro.PROJ_STATE_CODE
		
		projectstage = pro.PROJ_STAGE_DESC.string
		print pro.PROJ_STAGE_DESC
		
		projectcat = pro.PROJ_CAT1_DESC.string
		print pro.PROJ_CAT1_DESC

		projectstatus = pro.PROJ_STATUS_DESC.string
		print pro.PROJ_STATUS_DESC

		projectstart = pro.PROJ_START_DATE_DETAIL.string
		print pro.PROJ_START_DATE_DETAIL

		projectend = pro.PROJ_END_DATE_DETAIL.string
		print pro.PROJ_END_DATE_DETAIL
		
		projectvalue = float(pro.PROJ_VALUE.string)
		print pro.PROJ_VALUE

		projectvaldes= pro.PROJ_VALUE_DESC.string
		print pro.PROJ_VALUE_DESC

		projecttxt = pro.PROJ_DETAIL_TEXT.string
		print pro.PROJ_DETAIL_TEXT

		#add entry 
		new_entry = Project(city=city, location='', Project_ID=projectid, Project_Title=projecttitle, Project_Type=projectcipher, Project_Post=projectpost, Project_Suburb=projectsub, Project_State=projectstate,Project_Stage=projectstage,Project_Category=projectcat,PROJ_STATUST_DESC=projectstatus,PROJ_START_DATE_DETAIL=projectstart,PROJ_END_DATE_DETAIL=projectend,PROJ_VALUE=projectvalue,PROJ_VALUE_DESC=projectvaldes,PROJ_DETAIL_TEXT=projecttxt)
		new_entry.save()

#run function for testing
getprojectsdate()


