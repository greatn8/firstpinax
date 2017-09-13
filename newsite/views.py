from django.shortcuts import render
import django.views.generic
from django.http import HttpResponse
import urllib2

#for plot.ly
import plotly.plotly as py
import plotly.graph_objs as go

#for #django rest framework (only took 2 or 4 recommended)
from rest_framework.views import APIView
from rest_framework.response import Response


from newsite.models import Project
#Project = Project()

def index(request):

	myurl = "https://abr.business.gov.au/abrxmlsearchRPC/AbrXmlSearch.asmx/SearchByABNv201408?searchString=74172177893&includeHistoricalDetails=N&authenticationGuid=62301559-37d7-4505-8a1d-1c429ff09e63"
	myurl2= urllib2.Request(myurl)
	final = myurl2
	openermybet = urllib2.build_opener()	

	f2 = openermybet.open(myurl2)
	content2 = f2.read()

	return render(request, 'index.html')

	#final = type(content2)
	#print final
	#context = "hrll"
	#return render(request, 'index.html')

def ChartView(request):
		return render(request, 'charts.html')

def get_data(request, *args, **kwargs):
		data = {
			"Sales": 100,
			"customers" : 10,
		}
		return JsonResponse(data)

class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		data = {
			"Sales": 100,
			"customers" : 10,
			#gets count of pbject in Project model
			"projects": Project.objects.count(),
		}
		return Response(data)