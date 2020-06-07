from django.urls import path
from .views import CreateQuestion, QuestionDetails, AnswerDetails


urlpatterns = [
    path('question/', CreateQuestion.as_view(), name='create_question'),
    path('question/<int:pk>/', QuestionDetails.as_view(), name='question_details'),
    path('qanswer/', AnswerDetails.as_view(), name='answer_details'),
]
