from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # if we add something for the first parameter
    # the url will be : localhost:8000/polls/additional_parameter
    # the second parameter calls the specified view function with an
    # HttpRequest object as the first argument
    # the third parameter allows the URL to lbe referred to from elsewhere
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),


]
