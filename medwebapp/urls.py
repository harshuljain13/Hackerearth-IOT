__author__ = 'h_hack'
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^login/$',views.user_login,name='login'),
    url(r'^register/$',views.register, name='register'),
    url(r'^details/',views.detail_search),
    url(r'^getdetails/$',views.display_details,name='searchklop'),
    url(r'^(?P<kid>\w+[0-9]+)/$',views.klop_detail),
]