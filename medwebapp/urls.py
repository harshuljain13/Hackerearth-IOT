__author__ = 'h_hack'
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^details/',views.detail_search),
    url(r'^getdetails/$',views.display_details,name='searchklop'),
    url(r'^login/$',views.login),
    url(r'^validate/$',views.validate,name='validate'),
    url(r'^(?P<kid>\w+[0-9]+)/$',views.klop_detail),
]