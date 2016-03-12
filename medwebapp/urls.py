__author__ = 'h_hack'
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.user_login,name='login'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^register/$',views.register, name='register'),
    url(r'^watcher/(?P<watcher_id>\w+[0-9]+)/$',views.watcher_restapi),

    url(r'^watcher/dashboard/(?P<watcher_id>\w+[0-9]+)/$',views.watcher_dashboard,name='watcherdashboard'),
    url(r'^watcher/profile/(?P<watcher_id>\w+[0-9]+)/$',views.watcher_profile,name='watcherprofile'),
]