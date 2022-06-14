from django.urls import path
from . import views

urlpatterns = [
    # if we add something for the first parameter
    # the url will be : localhost:8000/polls/additional_parameter
    # the second parameter calls the specified view function with an
    # HttpRequest object as the first argument
    # the third parameter allows the URL to be referred to from elsewhere
    path('', views.index, name='index'),

]
