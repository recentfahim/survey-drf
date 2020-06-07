from rest_framework import serializers
from .models import Question, UserAnswer
from django.conf import settings


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'created_by']
        extra_kwargs = {'created_by': {'read_only': True}}


class UserAnswerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    question = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserAnswer
        fields = ['id', 'answer', 'question', 'user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['id', 'username', 'email', 'is_staff']
