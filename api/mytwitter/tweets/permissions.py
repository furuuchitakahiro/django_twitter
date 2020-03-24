from rest_framework import permissions

from .models import PublishStates


class PublishStatePermission(permissions.BasePermission):
    """

    """

    def has_object_permission(self, request, view, obj):
        # ツイートがグローバルに公開されている
        if obj.publish_state == PublishStates.GLOBAL.value[0]:
            return True

        # リクエストユーザーがログイン中かつ、ツイート主のフォロイーである
        if (
            not request.user.is_anonymous
            and obj.publish_state == PublishStates.PRIVATE.value[0]
            and request.user in obj.tweeter.followee.all()
        ):
            return True

        return False
