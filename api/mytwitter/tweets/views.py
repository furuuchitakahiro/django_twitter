from rest_framework import viewsets

from .models import Tweet
from .serializers import (
    ReadTweetSerializer,
    CreateTweetSerializer,
    UpdateTweetSerializer,
    ListReadTweetSerializer,
)


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        serializer_class = ReadTweetSerializer  # retrive
        if 'list' == self.action:
            serializer_class = ListReadTweetSerializer
        elif 'create' == self.action:
            serializer_class = CreateTweetSerializer
        elif self.action in ('update', 'partial_update'):
            serializer_class = UpdateTweetSerializer

        return serializer_class
