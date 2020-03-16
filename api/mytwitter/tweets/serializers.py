from typing import Dict, Any

from rest_framework import serializers

from .models import Tweet
from mytwitter_users.serializers import UserSerializer


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
            'like',
        )


class ReadTweetSerializer(TweetSerializer):
    """

    """

    class Meta(TweetSerializer.Meta):
        read_only_fields = TweetSerializer.Meta.fields


class CreateTweetSerializer(TweetSerializer):
    """

    """

    def create(self, validated_data: Dict[str, Any]):
        request = self.context.get('request', None)
        validated_data['tweeter'] = request.user
        return super().create(validated_data)


class UpdateTweetSerializer(TweetSerializer):
    """

    """
    # TODO: 実装


class ListReadTweetSerializer(serializers.ModelSerializer):
    """

    """

    # tweeter = UserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = (
            # 'tweeter',
            'slug',
            'body',
            'like',
            'publish_state',
        )
        read_only_fields = (
            # 'tweeter',
            'slug',
            'like',
        )


__all__ = [
    'ReadTweetSerializer',
    'CreateTweetSerializer',
    'UpdateTweetSerializer',
    'ListReadTweetSerializer',
]
