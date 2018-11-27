from django.shortcuts import render
from NewsTest.models import Employee
# Create your views here.
def home_page_view(request):
    return render(request, 'testapp/home.html')


def movie_news_view(request):
    news1="Telgu devas is not good" 
    news2="salman updating minimum 100 crore guarntee"
    news3="TOH is flopps movie"
    news4="anil kapoor is going to get "
    news5="devdas movies is banned "   
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    return render(request,'testapp/mnews.html',my_dict)


def employee_info_view(request):
    employees=Employee.objects.all()
    return render(request,'testapp/results.html',{'employees':employees})
 