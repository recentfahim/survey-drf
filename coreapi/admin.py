from django.contrib import admin
from .models import Question, UserAnswer
# Register your models here.
admin.site.register(Question)
admin.site.register(UserAnswer)
