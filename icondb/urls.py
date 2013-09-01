from django.views.generic import ListView, DetailView, TemplateView
from django.conf.urls.defaults import patterns, url
import models

def listView(base, model):
    return url(base+r'$', ListView.as_view(queryset=model.objects.all()))

def detailView(base, model):
    return url(base + r'/(?P<pk>\d+)$', DetailView.as_view(model=model))

urlpatterns = patterns('',
        url(r'^$', TemplateView.as_view(template_name='index.html')),
        listView(r'icons', models.Icon),
        detailView(r'icon', models.Icon),
        detailView(r'image', models.IconImage),
        listView(r'elements', models.Element),
        detailView(r'element', models.Element),
        listView(r'icontypes', models.IconType),
        detailView(r'icontype', models.IconType),
        listView(r'iconstyles', models.IconStyle),
        detailView(r'iconstyle', models.IconStyle),
        listView(r'location', models.LocationMaster),
        detailView(r'location', models.LocationMaster),
)
