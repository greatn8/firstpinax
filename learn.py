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
    	'password': "D2C30£9fe1^0C0B`2f8b",
    	
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
		print pro.PROJ_ADDRESS1

	#testing add entry working
	#new_entry = Project(city='chatswood', location='', Project_ID='', Project_Title='My project', Project_Type="Commerical", Project_Post="2067", Project_Suburb="Chatwood", Project_State="NSW",Project_Stage="Early",Project_Category="office",PROJ_STATUST_DESC="proceeding",PROJ_START_DATE_DETAIL="13081995",PROJ_END_DATE_DETAIL="14081999",PROJ_VALUE="1000000",PROJ_VALUE_DESC="1 million",PROJ_DETAIL_TEXT="Building an Office")
	#new_entry.save()

#run function for testing
getprojectsdate()


