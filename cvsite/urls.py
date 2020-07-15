from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.component_list, name='component_list'),
    url(r'^component/(?P<pk>[0-9]+)/$', views.component_detail, name='component_detail'),
    url(r'^component/(?P<pk>[0-9]+)/$', views.component_edit, name='component_edit'),
]