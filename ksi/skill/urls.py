from django.conf.urls import url
from . import views

urlpatterns = [
   url('',views.homepage),
   url('/about/',views.aboutpage),
    
]