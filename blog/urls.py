from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^cocktailslist/$', views.post_list, name='post_list'),
    url(r'^$', views.mood_list, name='homepage'),
    url(r'^happy/$', views.happy_list, name='happy_list'),
    url(r'^angry/$', views.angry_list, name='angry_list'),
    url(r'^sad/$', views.sad_list, name='sad_list'),
    url(r'^fun/$', views.fun_list, name='fun_list'),
    url(r'^excited/$', views.excited_list, name='excited_list'),
    url(r'^hungry/$', views.hungry_list, name='hungry_list'),
    url(r'^lazy/$', views.lazy_list, name='lazy_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
