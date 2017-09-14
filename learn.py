# -*- coding: utf-8 -*-
#! /usr/bin/env python

#this fixed app not installed error?!
import os,sys
import datetime

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
    	'username': "",
    	'password': "",
    	
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
	#base url
	#UAT http://projectsapi-UAT.cordell.com.au/api/Projects/ProjectGetAllData dont know what data is in there?
	url = "http://cordellprojectsapi.cordell.com.au/api/Projects/ProjectGetAllData"

	#manually adding date for now
	querystring = {"FROMDATE":"01/01/201","TODATE":"30/03/2013"}

	#addd header, uses finaltoken from token() function
	headers = {
    	'token': finaltoken,
    }

	response = requests.request("POST", url, headers=headers, params=querystring)
	resultraw = (response.text)
	print "Type Result Raw response",type(resultraw)

	resultrawstring = resultraw.encode('utf-8') # unicode to str

	#resultrawstring = str(resultraw)

	#makine string into soup and speicify its xml
	souprawresult = BeautifulSoup(resultrawstring, 'xml')
	
	#print type of souop
	print "soup type",type(souprawresult)

	#gets just project names
	projectnames = souprawresult.find_all('PROJ_TITLE')
	print projectnames
	print type(projectnames)

	#gets all projects in soup
	projectz = souprawresult.find_all('PROJECT')
	print projectz
	print type(projectz)
	
	#for eaach project get each field we want
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


		#my solution solution to get in right format dd-mm-yyyy from dd/mm/yy! :)
		projectsta = pro.PROJ_START_DATE_DETAIL.string
		projectstar2 = projectsta[:6] + '20' + projectsta[-2:]
		projectstart = datetime.datetime.strptime(projectstar2, "%d/%m/%Y").strftime("%Y-%m-%d")
		print pro.PROJ_START_DATE_DETAIL
		
		#my solution to get in right format dd-mm-yyyy from dd/mm/yy! :)
		projecten1 = pro.PROJ_END_DATE_DETAIL.string
		#solve no end date throwing error
		if projecten1 == None:
			projectend = "2999-12-12"
		else:	
			projecten2 = projecten1[:6] + '20' + projecten1[-2:]
			projectend = datetime.datetime.strptime(projecten2, "%d/%m/%Y").strftime("%Y-%m-%d")
			print pro.PROJ_END_DATE_DETAIL

		projectvalue = float(pro.PROJ_VALUE.string)
		print pro.PROJ_VALUE

		projectvaldes= pro.PROJ_VALUE_DESC.string
		print pro.PROJ_VALUE_DESC

		projecttxt = pro.PROJ_DETAIL_TEXT.string
		print pro.PROJ_DETAIL_TEXT

		#add entry with each field in our database being populated from previous
		new_entry = Project(city=city, location='', Project_ID=projectid, Project_Title=projecttitle, Project_Type=projectcipher, Project_Post=projectpost, Project_Suburb=projectsub, Project_State=projectstate,Project_Stage=projectstage,Project_Category=projectcat,PROJ_STATUST_DESC=projectstatus,PROJ_START_DATE_DETAIL=projectstart,PROJ_END_DATE_DETAIL=projectend,PROJ_VALUE=projectvalue,PROJ_VALUE_DESC=projectvaldes,PROJ_DETAIL_TEXT=projecttxt)
		#save the entry
		new_entry.save()

#run function for testing
getprojectsdate()


