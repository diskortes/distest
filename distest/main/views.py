from django.shortcuts import render_to_response
from distest.main.models import MyData

def show_mydata(request):
    my_data = MyData.objects.get(id=1)
    return render_to_response('mydata.html',{'data':my_data})
