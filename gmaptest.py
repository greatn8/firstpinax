import googlemaps
from datetime import datetime



gmaps = googlemaps.Client(key='')

geocode_result = gmaps.geocode('60-64 Advance St, Schofields, NSW')

print geocode_result
print "TYPE GEOCICODE RESULT:",type(geocode_result)

print "longitute & lattitude ",geocode_result[0]['geometry']['location']
print "longitute",geocode_result[0]['geometry']['location']['lng']
longy = geocode_result[0]['geometry']['location']['lat']
print type(longy)

