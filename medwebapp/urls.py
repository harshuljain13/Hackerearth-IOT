__author__ = 'h_hack'
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.user_login,name='login'),
    url(r'^accounts/login/',views.user_login),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^register/$',views.register, name='register'),

    url(r'^watcher2/(?P<watcher_id>\w+[0-9]+)/$',views.watcher_restapi2),
    url(r'^watcherpost/(?P<watcher_id>\w+[0-9]+)/rest/$',views.watcher_rest),

    url(r'^watcher/dashboard/(?P<watcher_id>\w+[0-9]+)/notactive/$',views.watcher_dashboard_notactive,name='watcherdashboardnotactive'),
    url(r'^watcher/dashboard/(?P<watcher_id>\w+[0-9]+)/$',views.watcher_dashboard,name='watcherdashboard'),

    url(r'^watcher/info/(?P<watcher_id>\w+[0-9]+)/$',views.watcher_info,name='watcherinfo'),
    url(r'^watcher/share/(?P<watcher_id>\w+[0-9]+)/$',views.watcher_share,name='watchershare'),
    url(r'^watcher/advice/(?P<watcher_id>\w+[0-9]+)/$',views.watcher_advicelist,name='advicelist'),
    url(r'^watcher/gadvice/(?P<watcher_id>\w+[0-9]+)/$',views.watcher_giveadvice,name='gadvice'),
    url(r'^watcher/profile/(?P<watcher_id>\w+[0-9]+)/$',views.profile_update,name='profileupdate'),
]