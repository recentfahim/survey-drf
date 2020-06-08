from rest_framework import serializers
from .models import Question, UserAnswer
from django.conf import settings


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'created_by']
        extra_kwargs = {'created_by': {'read_only': True}}


class UserAnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True, many=False)

    class Meta:
        model = UserAnswer
        fields = ['id', 'answer', 'question', 'user']
        extra_kwargs = {'user': {'read_only': True}}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['id', 'username', 'email', 'is_staff']
