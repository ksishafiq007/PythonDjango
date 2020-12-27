
from django.shortcuts import render
from .models import Myskill,Contactinfo

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
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('comments')
        #mydata=Contactinfo(cname=name,cemail=email,cquery=query)
        
        # or we can use with the below format.
        mydata=Contactinfo()
        mydata.cname=name
        mydata.cemail=email
        mydata.cquery=query

        mydata.save()
    
    return render(request,'contact.html')


# Create your views here.
