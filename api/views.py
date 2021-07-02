from django.shortcuts import render
from rest_framework import viewsets

from api.models import Poll
from api.permissions import IsAdminOrReadOnly
from api.serializer import PollsSerializer


class PollsViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollsSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()