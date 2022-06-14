import datetime

from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('publish date')

    def __str__(self):
        return f'Question : {self.question_text}, Publication date : {self.publication_date}\n'

    def was_published_recently(self) -> bool:
        return self.publication_date.timestamp() >= (timezone.now() - datetime.timedelta(days=1)).timestamp()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'Choice : {self.choice_text}, Votes : {self.votes}\n'
