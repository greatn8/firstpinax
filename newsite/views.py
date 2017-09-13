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
		data = {
			"Sales": 100,
			"customers" : 10,
			#gets count of pbject in Project model
			"projects": Project.objects.count(),
			"projectsQLD": Project.objects.all().filter(Project_State="QLD").count(),
			"projectsNSW": Project.objects.all().filter(Project_State="NSW").count()
		}	
		return Response(data)