
#imports
import requests
import urllib, json
import urllib2

#gets as string
def index():

	myurl = "https://abr.business.gov.au/abrxmlsearchRPC/AbrXmlSearch.asmx/SearchByABNv201408?searchString=74172177893&includeHistoricalDetails=N&authenticationGuid=62301559-37d7-4505-8a1d-1c429ff09e63"
	myurl2= urllib2.Request(myurl)
	openermybet = urllib2.build_opener()	

	f2 = openermybet.open(myurl)
	content2 = f2.read()
	print content2
	print type(content2)
	#context = "hrll"

#not working

def index1():
	myurl = "https://abr.business.gov.au/json/AbnDetails.aspx?abn=11016461277&callback=callback&guid=62301559-37d7-4505-8a1d-1c429ff09e63"
	response = urllib.urlopen(myurl)
	data = json.loads(response.read())
	#context = "hrll"
	for item in data:
	 	print item


#working detailed per abn
def index2():
	
	myurl = "https://abr.business.gov.au/abrxmlsearchRPC/AbrXmlSearch.asmx/SearchByABNv201408?searchString=74172177893&includeHistoricalDetails=N&authenticationGuid=62301559-37d7-4505-8a1d-1c429ff09e63"
	
	opener= urllib2.build_opener()	
	f2 = opener.open(myurl)
	content2 = f2.read()
	print content2
	print type(content2)
	#context = "hrll"
index2()	