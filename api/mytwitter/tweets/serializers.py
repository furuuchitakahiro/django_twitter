from typing import Dict, Any

from rest_framework import serializers

from .models import Tweet
from mytwitter.serialziers import UserSerializer


class TweetSerializer(serializers.ModelSerializer):
    """

    """

    tweeter = UserSerializer(read_only=True)
    
    class Meta:
        model = Tweet
        fields = (
            'tweeter',
            'slug',
            'body',
            'like',
            'publish_state',
        )
        read_only_fields = (
            'tweeter',
            'slug',
        )

    def create(self, validated_data: Dict[str, Any]):
        request = self.context.get('request', None)
        validated_data['tweeter'] = request.user
        return super().create(validated_data)
