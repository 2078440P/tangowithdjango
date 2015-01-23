from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!"
                        "<FONT COLOR = BLUE>"
                        "<A HREF = '/rango/about'> Here is the about page </A></FONT>")



def about(request):
    return HttpResponse("Rango says here is the about page."

                        "<FONT COLOR = BLUE>"
                        "<A HREF = '/rango'> Here is the home page </A></FONT>"
                        "This tutorial has been put together by Ben Procter, 2078440P" )
