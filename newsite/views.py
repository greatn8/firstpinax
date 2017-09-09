from django.shortcuts import render
from django.http import HttpResponse
import urllib2

def index(request):

	myurl = "https://abr.business.gov.au/abrxmlsearchRPC/AbrXmlSearch.asmx/SearchByABNv201408?searchString=74172177893&includeHistoricalDetails=N&authenticationGuid=62301559-37d7-4505-8a1d-1c429ff09e63"
	myurl2= urllib2.Request(myurl)
	#final = myurl2
	#openermybet = urllib2.build_opener()	

	#f2 = openermybet.open(myurl2)
	#content2 = f2.read()
	
	#final = type(content2)
	#print final
	context = "hrll"
	return render(request, 'index.html')

