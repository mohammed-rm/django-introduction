from django.contrib import admin
from .models import Question, Choice

# To add our model to Django admin panel
# on localhost:8000/admin
admin.site.register(Question)
admin.site.register(Choice)
