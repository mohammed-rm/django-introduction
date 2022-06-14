from django.contrib import admin
from .models import Question

# To add our model to Django admin panel
# on localhost:8000/admin
admin.site.register(Question)
