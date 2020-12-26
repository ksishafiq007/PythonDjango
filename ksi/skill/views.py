
from django.shortcuts import render

def homepage(request):
    title='Welcome to KSI bd'
    desc='I am KSI. I am a software developer'
    
    return render(request,'index.html',{'title':title,'description':desc})

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
