from django.http import HttpResponse
from django.http import HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    # Fetch last 5 question from database
    latest_question_list = Question.objects.order_by('-publication_date')[:5]

    response = ', '.join([q.question_text for q in latest_question_list])

    return HttpResponse(response)


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'You are looking at question : {question_id}')


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'You are looking at the results of question : {question_id}')


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question : {question_id}")