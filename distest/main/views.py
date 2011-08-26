from django.shortcuts import render_to_response
from distest.main.models import MyData, META_Data
from django.template import RequestContext
from distest.main.forms import EditData
from django.http import HttpResponseRedirect

def show_mydata(request):
    my_data = MyData.objects.get(id=1)
    return render_to_response('mydata.html',{'data':my_data})

def show_META(request):
    s_META = META_Data.objects.all()
    return render_to_response('mymeta.html',{'metas':s_META})

def processors(request):
    return render_to_response('processors.html',context_instance=RequestContext(request))

def change_data(request):
    form = EditData()
    if request.method =='POST':
        form = EditData(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            data=MyData.objects.get(id=1)
            if cd['name']: data.name=cd['name']
            if cd['last_name']: data.last_name=cd['last_name']
            if cd['bio']: data.bio=cd['bio']
            if cd['address']: data.address=cd['address']
            if cd['email']: data.email = cd['email']
            data.save()
            return HttpResponseRedirect('/')
        else:
            form = EditData()
    return render_to_response('edit.html',{'form':form})
