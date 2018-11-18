from django.urls import path
from testapp import views
urlpatterns = [
    path('first/',views.first_View),
    path('second/',views.second_View),
    path('third/',views.third_View),
    path('fourth/',views.fourth_View),
    path('fifth/',views.fifth_View),
]
