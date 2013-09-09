from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django import forms
from icondb.models import *

class IconImageForm(forms.ModelForm):
    class Meta:
        model = IconImage

def uploadImg(request):
    if request.method == 'POST':
        form = IconImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/icon/')
    else:
        form = IconImageForm()
    return render(request, 'imgform.html', {'form': form})
