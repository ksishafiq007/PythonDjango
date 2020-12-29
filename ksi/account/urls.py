from django.conf.urls import url
from .views import user_log,user_logout

urlpatterns = [
    url('',user_log, name='login'),
    url('logout/',user_logout, name='logout'),
]