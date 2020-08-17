from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def Home(request):
    Serv=Offers.objects.all()
    blog=Blogs.objects.all()
    serviceslider=Serviceslider.objects.all()
    return render(request,'Index.html',{'Serv':Serv , 'blog':blog,'serviceslider':serviceslider})
def Blog(request):
    vlog=Blogpage.objects.all()
    return render(request,'blog.html',{'vlog':vlog})
