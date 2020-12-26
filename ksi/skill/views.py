
from django.shortcuts import render
from .models import Myskill

def homepage(request):
    item=Myskill.objects.all()
    title='Welcome to KSI bd'
    desc='I am KSI. I am a software developer'
    context={
        'title':title,
        'description':desc,
        'data':item
    }
    
    return render(request,'index.html',context)

def aboutpage(request):
    title='About page for skill app'
    desc="""
          This is for about page description.
    """
    context={
        'title':title,
        'aboutdesc':desc,
    }
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')


# Create your views here.
