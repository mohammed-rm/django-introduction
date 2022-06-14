from django.http import HttpResponse
from django.http import HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, wold. Polls index.")
