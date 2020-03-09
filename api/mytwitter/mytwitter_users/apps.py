from django.apps import AppConfig
from django.db.models.signals import pre_save


class MytwitterUsersConfig(AppConfig):
    name = 'mytwitter_users'

    def ready(self):
        from mytwitter_users.models import User
        pre_save.connect(
            User._pre_save_handler,
            sender=User
        )
