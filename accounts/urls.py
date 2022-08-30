import cmd
from django.conf.urls import url
from accounts import views 
from django.urls import path

 
urlpatterns = [ 
    url(r'^staff$', views.staffAPI),
    url(r'^create$', views.createStaff),
    url(r'^update$', views.updateStaff),
    url(r'^delete/([0-9]+)$', views.deleteStaff),
    
]


 
  