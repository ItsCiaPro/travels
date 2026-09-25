from django.shortcuts import render, HttpResponse

# Create your views here
def attractions(req):
   return render(req, "app_josue/attractions.html")

def identity(req):
   return render(req, "app_josue/identity.html")

def pictures(req):
   return render(req, "app_josue/pictures.html")