from django.shortcuts import render
from django.conf import settings

GOOGLE_MAPS_API_KEY = settings.GOOGLE_MAPS_API_KEY


def about(request):                  
    """ render the about page and import google maps api key"""

    context = {
    
    'about': 'active',
    'GOOGLE_MAPS_API_KEY' : settings.GOOGLE_MAPS_API_KEY
    
    }
    
   
    return render(request, 'about.html', context)