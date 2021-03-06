from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.LoginView, name='login'),
    url(r'^loginhandle$', views.LoginHandleView, name='loginhandle'),
    #url(r'^(?P<user_id>[0-9]+)/event/$', views.EventView, name='event'),
    url(r'^(?P<user_id>[0-9]+)/cat/$', views.catView, name='catalog'),
    #url(r'^(?P<user_id>[0-9]+)/search/$', views.searchView, name='search'),
    #url(r'^(?P<user_id>[0-9]+)/rec/$', views.recommendView, name='reccomend'),
    url(r'^(?P<user_id>[0-9]+)/orders/$', views.orderView, name='orders'),
    url(r'^(?P<user_id>[0-9]+)/buy/$', views.createBuyView, name='buyItem'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
