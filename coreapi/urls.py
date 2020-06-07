from django.urls import path
from .views import CreateQuestion, QuestionDetails


urlpatterns = [
    path('question/', CreateQuestion.as_view(), name='create_question'),
    path('question/<int:pk>/', QuestionDetails.as_view(), name='question_details'),
]
