from django.conf.urls import url
from . import views

urlpatterns = [
   url('',views.homepage, name='home'),
   url('about/',views.aboutpage, name='about'),
   url('contact/',views.contactpage, name='contact'),
    
]