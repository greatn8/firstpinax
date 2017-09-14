from django.shortcuts import render
import django.views.generic
from django.http import HttpResponse
import urllib2
import datetime 

#for plot.ly
import plotly.plotly as py
import plotly.graph_objs as go

#for #django rest framework (only took 2 or 4 recommended)
from rest_framework.views import APIView
from rest_framework.response import Response


from newsite.models import Project
#Project = Project()

def index(request):


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

#chartdata view no template.html required -->  see url
class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		#provide label data for label field below
		QLD_count = Project.objects.all().filter(Project_State="QLD").count()
		labels = ["QLD Projects", "Blue", "Yellow", "Green", "Purple", "Orange"]
		default_items = [QLD_count, 500, 654, 343, 455, 600 ]
		#data to return in json format
		data = {
			"labels": labels,
			"default": default_items,
			#gets count of pbject in Project model
			"projects": Project.objects.count(),
			#count all projecst in QLD
			"projectsQLD": Project.objects.all().filter(Project_State="QLD").count(),
			#count all projects in NSW
			"projectsNSW": Project.objects.all().filter(Project_State="NSW").count(),
			"projectsVIC": Project.objects.all().filter(Project_State="VIC").count(),
			#projectsstarting month and state can be modified with more filters
			"ProjectsQLDstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-09-01', PROJ_START_DATE_DETAIL__gt='2017-07-01',Project_State="QLD").count(),
		}	
		return Response(data)