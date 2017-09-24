from django.shortcuts import render
import django.views.generic
from django.http import HttpResponse
from django.db.models import Avg
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

def TestView(request):
		return render(request, 'testing.html')		

def CommenceView(request):
		return render(request, 'commencing.html')			

def AbandonedView(request):
		return render(request, 'abandoned.html')			

def NewProjectsView(request):
		return render(request, 'newprojects.html')			

def NewProjectsView2(request):
		return render(request, 'newprojects2.html')			


def get_data(request, *args, **kwargs):
		data = {
			"Sales": 100,
			"customers" : 10,
		}
		return JsonResponse(data)

#first chart no template.html required -->  see url
class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		QLD_count = Project.objects.all().filter(Project_State="QLD").count()
		#for QLD started construction over 12 months 2017
		ProjectsQLDJANstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-02-01', PROJ_START_DATE_DETAIL__gte='2017-01-01',Project_State="QLD").count(),
		ProjectsQLDFEBstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-03-01', PROJ_START_DATE_DETAIL__gte='2017-02-01',Project_State="QLD").count(),
		ProjectsQLDMARstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-04-01', PROJ_START_DATE_DETAIL__gte='2017-03-01',Project_State="QLD").count(),
		ProjectsQLDAPRstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-05-01', PROJ_START_DATE_DETAIL__gte='2017-04-01',Project_State="QLD").count(),
		ProjectsQLDMAYstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-06-01', PROJ_START_DATE_DETAIL__gte='2017-05-01',Project_State="QLD").count(),
		ProjectsQLDJUNstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-07-01', PROJ_START_DATE_DETAIL__gte='2017-06-01',Project_State="QLD").count(),
		ProjectsQLDJULstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-08-01', PROJ_START_DATE_DETAIL__gte='2017-07-01',Project_State="QLD").count(),
		ProjectsQLDAUGstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-09-01', PROJ_START_DATE_DETAIL__gte='2017-08-01',Project_State="QLD").count(),
		ProjectsQLDSEPstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-10-01', PROJ_START_DATE_DETAIL__gte='2017-09-01',Project_State="QLD").count(),
		ProjectsQLDOCTstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-11-01', PROJ_START_DATE_DETAIL__gte='2017-10-01',Project_State="QLD").count(),
		ProjectsQLDNOVstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-12-01', PROJ_START_DATE_DETAIL__gte='2017-11-01',Project_State="QLD").count(),
		ProjectsQLDDECstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-01-01', PROJ_START_DATE_DETAIL__gte='2017-12-01',Project_State="QLD").count(),

		#for QLD started construction over 12 months 2018
		ProjectsQLDJAN18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-02-01', PROJ_START_DATE_DETAIL__gte='2018-01-01',Project_State="QLD").count(),
		ProjectsQLDFEB18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-03-01', PROJ_START_DATE_DETAIL__gte='2018-02-01',Project_State="QLD").count(),
		ProjectsQLDMAR18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-04-01', PROJ_START_DATE_DETAIL__gte='2018-03-01',Project_State="QLD").count(),
		ProjectsQLDAPR18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-05-01', PROJ_START_DATE_DETAIL__gte='2018-04-01',Project_State="QLD").count(),
		ProjectsQLDMAY18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-06-01', PROJ_START_DATE_DETAIL__gte='2018-05-01',Project_State="QLD").count(),
		ProjectsQLDJUN18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-07-01', PROJ_START_DATE_DETAIL__gte='2018-06-01',Project_State="QLD").count(),
		ProjectsQLDJUL18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-08-01', PROJ_START_DATE_DETAIL__gte='2018-07-01',Project_State="QLD").count(),
		ProjectsQLDAUG18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-09-01', PROJ_START_DATE_DETAIL__gte='2018-08-01',Project_State="QLD").count(),
		ProjectsQLDSEP18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-10-01', PROJ_START_DATE_DETAIL__gte='2018-09-01',Project_State="QLD").count(),
		ProjectsQLDOCT18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-11-01', PROJ_START_DATE_DETAIL__gte='2018-10-01',Project_State="QLD").count(),
		ProjectsQLDNOV18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-12-01', PROJ_START_DATE_DETAIL__gte='2018-11-01',Project_State="QLD").count(),
		ProjectsQLDDEC18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2019-01-01', PROJ_START_DATE_DETAIL__gte='2018-12-01',Project_State="QLD").count(),


		#for NSW started construction over 12 months 2017
		ProjectsNSWJANstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-02-01', PROJ_START_DATE_DETAIL__gte='2017-01-01',Project_State="NSW").count(),
		ProjectsNSWFEBstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-03-01', PROJ_START_DATE_DETAIL__gte='2017-02-01',Project_State="NSW").count(),
		ProjectsNSWMARstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-04-01', PROJ_START_DATE_DETAIL__gte='2017-03-01',Project_State="NSW").count(),
		ProjectsNSWAPRstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-05-01', PROJ_START_DATE_DETAIL__gte='2017-04-01',Project_State="NSW").count(),
		ProjectsNSWMAYstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-06-01', PROJ_START_DATE_DETAIL__gte='2017-05-01',Project_State="NSW").count(),
		ProjectsNSWJUNstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-07-01', PROJ_START_DATE_DETAIL__gte='2017-06-01',Project_State="NSW").count(),
		ProjectsNSWJULstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-08-01', PROJ_START_DATE_DETAIL__gte='2017-07-01',Project_State="NSW").count(),
		ProjectsNSWAUGstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-09-01', PROJ_START_DATE_DETAIL__gte='2017-08-01',Project_State="NSW").count(),
		ProjectsNSWSEPstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-10-01', PROJ_START_DATE_DETAIL__gte='2017-09-01',Project_State="NSW").count(),
		ProjectsNSWOCTstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-11-01', PROJ_START_DATE_DETAIL__gte='2017-10-01',Project_State="NSW").count(),
		ProjectsNSWNOVstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-12-01', PROJ_START_DATE_DETAIL__gte='2017-11-01',Project_State="NSW").count(),
		ProjectsNSWDECstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-01-01', PROJ_START_DATE_DETAIL__gte='2017-12-01',Project_State="NSW").count(),
		
		#for NSW started construction over 12 months 2018
		ProjectsNSWJAN18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-02-01', PROJ_START_DATE_DETAIL__gte='2018-01-01',Project_State="NSW").count(),
		ProjectsNSWFEB18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-03-01', PROJ_START_DATE_DETAIL__gte='2018-02-01',Project_State="NSW").count(),
		ProjectsNSWMAR18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-04-01', PROJ_START_DATE_DETAIL__gte='2018-03-01',Project_State="NSW").count(),
		ProjectsNSWAPR18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-05-01', PROJ_START_DATE_DETAIL__gte='2018-04-01',Project_State="NSW").count(),
		ProjectsNSWMAY18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-06-01', PROJ_START_DATE_DETAIL__gte='2018-05-01',Project_State="NSW").count(),
		ProjectsNSWJUN18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-07-01', PROJ_START_DATE_DETAIL__gte='2018-06-01',Project_State="NSW").count(),
		ProjectsNSWJUL18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-08-01', PROJ_START_DATE_DETAIL__gte='2018-07-01',Project_State="NSW").count(),
		ProjectsNSWAUG18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-09-01', PROJ_START_DATE_DETAIL__gte='2018-08-01',Project_State="NSW").count(),
		ProjectsNSWSEP18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-10-01', PROJ_START_DATE_DETAIL__gte='2018-09-01',Project_State="NSW").count(),
		ProjectsNSWOCT18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-11-01', PROJ_START_DATE_DETAIL__gte='2018-10-01',Project_State="NSW").count(),
		ProjectsNSWNOV18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-12-01', PROJ_START_DATE_DETAIL__gte='2018-11-01',Project_State="NSW").count(),
		ProjectsNSWDEC18start = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2019-01-01', PROJ_START_DATE_DETAIL__gte='2018-12-01',Project_State="NSW").count(),
		
		#!average values of qLD retial,warehoujes... used for sectors and categories
		showrooms_countQLD = Project.objects.all().filter(Project_Category="SHOWROOMS, RETAIL WAREHOUSES, RETAIL MARKETS, BULKY GOODS",Project_State="QLD" ).aggregate(Avg('PROJ_VALUE')),	
		showrooms_countQLD2 = round(showrooms_countQLD[0]['PROJ_VALUE__avg']) * 1000

		#provides gelocations for first heatmap
		ProjectsQLD14startheat = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2014-12-31', PROJ_START_DATE_DETAIL__gte='2014-01-01',Project_State="QLD").values_list('location', flat=True),
		

		#SHOPS, SHOPPING CENTRES & ARCADES, SUPERMARKETS
		#provide label data for label field below
		labels = ["Commercial", "Industrial", "Community", "Residential", "Civil"]
		#used on commencing page for by sector graph
		default_items = [530, 400, 654, 700, 655]
		default_items2 = [630, 550, 404, 650, 635]


		QLDmedCat_items = [5264842, 4652842, 6524832, 5731548, 5601542]
		NSWmedCat_items2 = [6325426, 5456284, 4658425, 6654351, 3315841]

		Hospitalityavgval = [6325426, 5456284, 4658425, 6654351, 3315841, 2372643, 5376256]
		Hospitalityavgval17 = [5325426, 4456284, 5658425, 3654351, 4315841, 3372643, 4376256]
		Hospitalitylabels = ["Hotels, Serviced Apartment", "Motels, Bed & Breakfast, Cabins","Backpacker Accomodation", "Restaurants, Canteens","Take-away Outlets", "Conference & Reception Centres & Facilities", "Clubs (licensed),Casinos,Tavers"]
		
		Educationavg17 = [3364324, 1605462, 9753842]
		Educationlabels = ["Schools - Upto Year 12", "Childcare, Day Nurseries", "Tertiary - Universities, Colleges"]

		labelsqldcom17 = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		#qld commence 17 to be returned in json format below
		QLDCommence17 = [ProjectsQLDJANstart, ProjectsQLDFEBstart, ProjectsQLDMARstart, ProjectsQLDAPRstart, ProjectsQLDMAYstart, ProjectsQLDJUNstart, ProjectsQLDJULstart, ProjectsQLDAUGstart, ProjectsQLDSEPstart, ProjectsQLDOCTstart, ProjectsQLDNOVstart, ProjectsQLDDECstart]
		#qld commence 18 to be returned in json format below
		QLDCommence18 = [ProjectsQLDJAN18start, ProjectsQLDFEB18start, ProjectsQLDMAR18start, ProjectsQLDAPR18start, ProjectsQLDMAY18start, ProjectsQLDJUN18start, ProjectsQLDJUL18start, ProjectsQLDAUG18start, ProjectsQLDSEP18start, ProjectsQLDOCT18start, ProjectsQLDNOV18start, ProjectsQLDDEC18start]
		#new commence 17 to be returned in json format below
		NSWCommence17 = [ProjectsNSWJANstart, ProjectsNSWFEBstart, ProjectsNSWMARstart, ProjectsNSWAPRstart, ProjectsNSWMAYstart, ProjectsNSWJUNstart, ProjectsNSWJULstart, ProjectsNSWAUGstart, ProjectsNSWSEPstart, ProjectsNSWOCTstart, ProjectsNSWNOVstart, ProjectsNSWDECstart]
		#new commence 18 to be returned in json format below
		NSWCommence18 = [ProjectsNSWJAN18start, ProjectsNSWFEB18start, ProjectsNSWMAR18start, ProjectsNSWAPR18start, ProjectsNSWMAY18start, ProjectsNSWJUN18start, ProjectsNSWJUL18start, ProjectsNSWAUG18start, ProjectsNSWSEP18start, ProjectsNSWOCT18start, ProjectsNSWNOV18start, ProjectsNSWDEC18start]
		

		#data to return in json format
		data = {
			"labels": labels,
			"default": default_items,
			"default2": default_items2,

			"Educationavg17" : Educationavg17,
			"Educationlabels" : Educationlabels,
			#hospitality chart
			"Hospitalityavgval" : Hospitalityavgval,
			"Hospitalityavgval17" : Hospitalityavgval17,
			"Hospitalitylabels" : Hospitalitylabels,
			#QLD Commence 2017 	
			"QLDCommence17": QLDCommence17,
			#QLD Commence 2018 	
			"QLDCommence18": QLDCommence18,
			#NSW Commence 2017 	
			"NSWCommence17": NSWCommence17,
			#NSW Commence 2017 	
			"NSWCommence18": NSWCommence18,

			"labelsqldcom17": labelsqldcom17,
			#gets count of pbject in Project model
			"projects": Project.objects.count(),
			#count all projecst in QLD
			"projectsQLD": Project.objects.all().filter(Project_State="QLD").count(),
			#count all projects in NSW
			"projectsNSW": Project.objects.all().filter(Project_State="NSW").count(),
			"projectsVIC": Project.objects.all().filter(Project_State="VIC").count(),
			#projectsstarting month and state can be modified with more filters yyyy-mm-dd - this QLD JAN commencemnt
			"ProjectsQLDJANstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-02-01', PROJ_START_DATE_DETAIL__gte='2017-01-01',Project_State="QLD").count(),
			"ProjectsQLDFEBstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-03-01', PROJ_START_DATE_DETAIL__gte='2017-02-01',Project_State="QLD").count(),
			"ProjectsQLDMARstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-04-01', PROJ_START_DATE_DETAIL__gte='2017-03-01',Project_State="QLD").count(),
			"ProjectsQLDAPRstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-05-01', PROJ_START_DATE_DETAIL__gte='2017-04-01',Project_State="QLD").count(),
			"ProjectsQLDMAYstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-06-01', PROJ_START_DATE_DETAIL__gte='2017-05-01',Project_State="QLD").count(),
			"ProjectsQLDJUNstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-07-01', PROJ_START_DATE_DETAIL__gte='2017-06-01',Project_State="QLD").count(),
			"ProjectsQLDJULstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-08-01', PROJ_START_DATE_DETAIL__gte='2017-07-01',Project_State="QLD").count(),
			"ProjectsQLDAUGstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-09-01', PROJ_START_DATE_DETAIL__gte='2017-08-01',Project_State="QLD").count(),
			"ProjectsQLDSEPstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-10-01', PROJ_START_DATE_DETAIL__gte='2017-09-01',Project_State="QLD").count(),
			"ProjectsQLDOCTstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-11-01', PROJ_START_DATE_DETAIL__gte='2017-10-01',Project_State="QLD").count(),
			"ProjectsQLDNOVstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-12-01', PROJ_START_DATE_DETAIL__gte='2017-11-01',Project_State="QLD").count(),
			"ProjectsQLDDECstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-01-01', PROJ_START_DATE_DETAIL__gte='2017-12-01',Project_State="QLD").count(),
		
			"ProjectsNSWJANstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-02-01', PROJ_START_DATE_DETAIL__gte='2017-01-01',Project_State="NSW").count(),

			"showrooms_countQLD": showrooms_countQLD,
			"QLDmedCat_items" : QLDmedCat_items,
			"NSWmedCat_items2" : NSWmedCat_items2,
			
			"showrooms_countQLD" : showrooms_countQLD2,

			#first qld heat map projects commencing in 2014 
			"ProjectsQLD14startheat" : ProjectsQLD14startheat[0],
		}	


		return Response(data)
# QLD Commencemnt Chart
# class Chart2(APIView):
# 	authentication_classes = []
# 	permission_classes = []

# 	def get(self, request, format=None):
# 		#provide label data for label field below
# 		ProjectsQLDJANstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-02-01', PROJ_START_DATE_DETAIL__gte='2017-01-01',Project_State="QLD").count(),

# 		ProjectsQLDFEBstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-03-01', PROJ_START_DATE_DETAIL__gte='2017-02-01',Project_State="QLD").count(),
# 		ProjectsQLDMARstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-04-01', PROJ_START_DATE_DETAIL__gte='2017-03-01',Project_State="QLD").count(),
# 		ProjectsQLDAPRstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-05-01', PROJ_START_DATE_DETAIL__gte='2017-04-01',Project_State="QLD").count(),
# 		ProjectsQLDMAYstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-06-01', PROJ_START_DATE_DETAIL__gte='2017-05-01',Project_State="QLD").count(),
# 		ProjectsQLDJUNstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-07-01', PROJ_START_DATE_DETAIL__gte='2017-06-01',Project_State="QLD").count(),
# 		ProjectsQLDJULstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-08-01', PROJ_START_DATE_DETAIL__gte='2017-07-01',Project_State="QLD").count(),
# 		ProjectsQLDAUGstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-09-01', PROJ_START_DATE_DETAIL__gte='2017-08-01',Project_State="QLD").count(),
# 		ProjectsQLDSEPstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-10-01', PROJ_START_DATE_DETAIL__gte='2017-09-01',Project_State="QLD").count(),
# 		ProjectsQLDOCTstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-11-01', PROJ_START_DATE_DETAIL__gte='2017-10-01',Project_State="QLD").count(),
# 		ProjectsQLDNOVstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-12-01', PROJ_START_DATE_DETAIL__gte='2017-11-01',Project_State="QLD").count(),
# 		ProjectsQLDDECstart = Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-01-01', PROJ_START_DATE_DETAIL__gte='2017-12-01',Project_State="QLD").count(),

# 		labels = ["QLD Projects", "Blue", "Yellow", "Green", "Purple", "Orange"]
# 		default_items = [ProjectsQLDJANstart, ProjectsQLDFEBstart, ProjectsQLDMARstart ]
# 		#data to return in json format
# 		data = {
# 			"labels": labels,
# 			"default": default_items,
# 			#gets count of pbject in Project model
# 			"projects": Project.objects.count(),
# 			#count all projecst in QLD
# 			"projectsQLD": Project.objects.all().filter(Project_State="QLD").count(),
# 			#count all projects in NSW
# 			"projectsNSW": Project.objects.all().filter(Project_State="NSW").count(),
# 			"projectsVIC": Project.objects.all().filter(Project_State="VIC").count(),
# 			#projectsstarting month and state can be modified with more filters yyyy-mm-dd - this QLD JAN commencemnt
# 			"ProjectsQLDJANstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-02-01', PROJ_START_DATE_DETAIL__gte='2017-01-01',Project_State="QLD").count(),
# 			"ProjectsQLDJFEBstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-03-01', PROJ_START_DATE_DETAIL__gte='2017-02-01',Project_State="QLD").count(),
# 			"ProjectsQLDMARstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-04-01', PROJ_START_DATE_DETAIL__gte='2017-03-01',Project_State="QLD").count(),
# 			"ProjectsQLDAPRstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-05-01', PROJ_START_DATE_DETAIL__gte='2017-04-01',Project_State="QLD").count(),
# 			"ProjectsQLDMAYstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-06-01', PROJ_START_DATE_DETAIL__gte='2017-05-01',Project_State="QLD").count(),
# 			"ProjectsQLDJUNstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-07-01', PROJ_START_DATE_DETAIL__gte='2017-06-01',Project_State="QLD").count(),
# 			"ProjectsQLDJULstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-08-01', PROJ_START_DATE_DETAIL__gte='2017-07-01',Project_State="QLD").count(),
# 			"ProjectsQLDAUGstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-09-01', PROJ_START_DATE_DETAIL__gte='2017-08-01',Project_State="QLD").count(),
# 			"ProjectsQLDSEPstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-10-01', PROJ_START_DATE_DETAIL__gte='2017-09-01',Project_State="QLD").count(),
# 			"ProjectsQLDOCTstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-11-01', PROJ_START_DATE_DETAIL__gte='2017-10-01',Project_State="QLD").count(),
# 			"ProjectsQLDNOVstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2017-12-01', PROJ_START_DATE_DETAIL__gte='2017-11-01',Project_State="QLD").count(),
# 			"ProjectsQLDDECstart": Project.objects.filter(PROJ_START_DATE_DETAIL__lt='2018-01-01', PROJ_START_DATE_DETAIL__gte='2017-12-01',Project_State="QLD").count(),
# 		}	
# 		return Response(data)		