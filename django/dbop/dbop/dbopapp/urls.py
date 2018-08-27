from django.conf.urls import url, include
from .import views

urlpatterns = [
   url(r'^employeetable/$',views.emp_table,name = 'emp_table'),
   url(r'^update/(?P<id>[0-9]+)/$',views.update_emp, name ='update_emp'),
   url(r'^delete/(?P<id>[0-9]+)/$',views.delete,name = 'delete'),
   url(r'^createemployee/$',views.create_emp, name = 'create_emp'),
]