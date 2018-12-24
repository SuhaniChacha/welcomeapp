from django.conf.urls import url , include
from . import  views


urlpatterns = [

    url(r'^page1',views.welcomepage, name='welcomepage'),

]