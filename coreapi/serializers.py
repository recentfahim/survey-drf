from rest_framework import serializers
from .models import Question, UserAnswer
from django.conf import settings


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text']

    def create(self, validated_data):
        question = Question(question_text=validated_data['question_text'])
        question.save()
        return question


class UserAnswerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    question = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserAnswer
        fields = ['id', 'answer', 'question', 'user']

    def create(self, validated_data):
        answer = UserAnswer(
            answer=validated_data['answer'],
            question=validated_data['question'],
            user=validated_data['user']
        )
        answer.save()
        return answer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['id', 'username', 'email', 'is_staff']
