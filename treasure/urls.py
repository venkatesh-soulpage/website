from django.conf.urls import url
from . import views 
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^user/(\w+)/$',views.profile,name='profile'),
    url(r'^$',views.index,name = 'index'),
    url(r'^([0-9]+)/$', views.detail,name = 'detail'),
    url(r'^user/(\w+)/post_url/$',views.post_treasure,name='post_treasure'),
    url(r'^login/$',views.login_view,name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^like_treasure/$',views.like_treasure,name='like_treasure'),
    url(r'^signup/$',views.signup, name='signup'),
     
]

if settings.DEBUG:
	urlpatterns+=[
	url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),
	]
