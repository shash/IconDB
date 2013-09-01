from django.views.generic import ListView, DetailView
from django.conf.urls import patterns, url
import models

urlpatterns = patterns('',
        url(r'icons$', ListView.as_view(
                queryset=models.Icon.objects.all())),
        url(r'icon/(?P<pk>\d+)$',
            DetailView.as_view(
                model=models.Icon)),
        url(r'image/(?P<pk>\d+)$',
            DetailView.as_view(
                model=models.IconImage)),
        )
