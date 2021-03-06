from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

"""
Creates new URLs for different pages on the site and uses the assigned view to request content
"""

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^cocktailslist/$', views.post_list, name='post_list'),
    url(r'^happy/$', views.happy_list, name='happy_list'),
    url(r'^fun/$', views.fun_list, name='fun_list'),
    url(r'^excited/$', views.excited_list, name='excited_list'),
    url(r'^hungry/$', views.hungry_list, name='hungry_list'),
    url(r'^lazy/$', views.lazy_list, name='lazy_list'),
    url(r'^tired/$', views.tired_list, name='tired_list'),
    url(r'^party/$', views.party_list, name='party_list'),
    url(r'^fancy/$', views.fancy_list, name='fancy_list'),
    url(r'^pitcher/$', views.pitcher_list, name='pitcher_list'),
    url(r'^flirty/$', views.flirty_list, name='flirty_list'),
    url(r'^surprise/$', views.surprise_me, name='surprise_me'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^search/$', views.search, name='search'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^nonalcoholic/$', views.non_alcoholic, name='non_alcoholic'),

]
