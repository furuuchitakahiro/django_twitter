from rest_framework import viewsets

from .models import Tweet
from .serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    lookup_field = 'slug'
    serializer_class = TweetSerializer
