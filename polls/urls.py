from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # if we add something for the first parameter
    # the url will be : localhost:8000/polls/additional_parameter
    # the second parameter calls the specified view function with an
    # HttpRequest object as the first argument
    # the third parameter allows the URL to lbe referred to from elsewhere
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
