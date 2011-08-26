from django.shortcuts import render_to_response
from distest.main.models import MyData, META_Data

def show_mydata(request):
    my_data = MyData.objects.get(id=1)
    return render_to_response('mydata.html',{'data':my_data})

def show_META(request):
    s_META = META_Data.objects.all()
    return render_to_response('mymeta.html',{'metas':s_META})
