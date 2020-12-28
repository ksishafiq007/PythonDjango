from django.conf.urls import url
from .views import user_log

urlpatterns = [
    url('',user_log, name='login'),
]