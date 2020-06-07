from django.db import models
from generic.models import BaseModel
from .enums import AnswerChoice
from django.conf import settings


class Question(BaseModel):
    question_text = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'

    def __str__(self):
        return self.question_text


class UserAnswer(BaseModel):
    answer = models.CharField(max_length=3, choices=[(answer.value, answer.name) for answer in AnswerChoice])
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='%(class)s_question')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_user')

    class Meta:
        verbose_name = 'user_answer'
        verbose_name_plural = 'user_answers'

    def __str__(self):
        return self.user.username + ' - ' + self.answer + ' - ' + self.question.question_text
