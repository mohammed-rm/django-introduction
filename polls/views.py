from django.http import HttpResponse
from django.http import HttpRequest
from django.http import Http404
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404


def index(request: HttpRequest) -> HttpResponse:
    # Fetch last 5 question from database
    latest_question_list = Question.objects.order_by('-publication_date')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'You are looking at the results of question : {question_id}')


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question : {question_id}")
