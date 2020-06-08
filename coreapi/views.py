from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from .serializers import QuestionSerializer, UserAnswerSerializer, ReadUserAnswerSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Question, UserAnswer
from django.http import Http404


class CreateQuestion(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        questions = Question.objects.all().order_by('created_at')
        serializers = QuestionSerializer(questions, many=True)

        context = {
            'message': 'All questions',
            'data': serializers.data,
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetails(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = UserAnswer.objects.filter(user=request.user)
        serializer = ReadUserAnswerSerializer(queryset, many=True)
        context = {
            'message': 'Your answers',
            'data': serializer.data,
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
