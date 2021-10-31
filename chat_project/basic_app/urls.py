from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from basic_app import views
from django.contrib.auth import views as auth_views

app_name = 'basic_app'

urlpatterns = [
    url(r'^signup/$',views.SignUpView.as_view(),name='signup'),
    url(r'^login/$',views.login_user,name = 'login'),
    # url(r'^login/$',auth_views.LoginView.as_view(template_name = 'basic_app/login.html'),name = 'login'),
    url(r'^user/',views.LoginLandingView.as_view(),name='user'),
    url(r'^logout/',views.logout_user,name='logout'),
    url(r'^newpost/$',views.PostView.as_view(),name='newpost'),
    url(r'^newgroup/$',views.GroupView.as_view(),name='newgroup'),
    url(r'^groups/$',views.GroupListView.as_view(),name='groups'),
    url(r'^detail/(?P<pk>[-\w]+)/$',views.JoinDetailView.as_view(),name='join'),
    url(r'^leavedetail/(?P<pk>[-\w]+)/$',views.leave_view,name='leave'),
    url(r'^backtodetail/(?P<pk>[-\w]+)/$',views.joinback_view,name='joinback'),
    url(r'^postsingroup/(?P<pk>[-\w]+)/$',views.PostsInGroupView.as_view(),name='postsingroup'),
    url(r'^deletepost/(?P<pk>[-\w]+)/$',views.DeleteOptionPage.as_view(),name='deletepost'),
    url(r'^allposts/$',views.AllPostsView.as_view(),name='allposts'),
    url(r'^postbts/(?P<pk>[-\w]+)/$',views.nondisplay_view,name='nondisplaysetup'),
    url(r'^postdeletebts/(?P<pk>[-\w]+)/$',views.post_deleteview,name='postdeletebts'),
    url(r'^curruserpost/(?P<pk>[-\w]+)/$',views.grab_userview,name='curruserpost'),
]
