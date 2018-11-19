from django.shortcuts import render
import datetime
# Create your views here.
def template_view(request):
      dt=datetime.datetime.now()
    #   my_dict={'date':dt}
    #   return render(request,'testapp/results.html',context=my_dict)
      name='Durga'
      rollno=101
      marks=100
      my_dict={'time':dt,'name':name,'rollno':rollno,'marks':marks}
      h=int(dt.strftime('%H'))
      
      if h<12:
        return render(request,'testapp/morning.html', my_dict)

      if h<16:
        return render(request,'testapp/afternoon.html',my_dict)
      if h<21:
        return render(request,'testapp/evening.html',my_dict)
      else:
        return render(request,'testapp/night.html', my_dict)
       
      # return render(request,'testapp/results.html',{'time':dt},my_dict)
