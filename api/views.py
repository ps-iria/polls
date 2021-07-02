from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Poll, Question, Vote, Choice, Answer
from api.permissions import IsAdminOrReadOnly, IsAdmin
from api.serializer import PollsSerializer, QuestionsSerializer, \
    VotesSerializer, ChoiceSerializer

User = get_user_model()

class PollsViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollsSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = (IsAdmin,)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VotesSerializer
    http_method_names = ('get', 'post')

    def get_queryset(self):
        queryset = Vote.objects.filter(user=self.request.user).all()
        return queryset

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            return serializer.save(user=self.request.user)

        return super().perform_create(serializer)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = ChoiceSerializer
