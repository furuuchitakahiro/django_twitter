from django.apps import AppConfig
from django.db.models.signals import pre_save


class TweetsConfig(AppConfig):
    name = 'tweets'

    def ready(self):
        from tweets.models import Tweet
        pre_save.connect(
            Tweet._pre_save_handler,
            sender=Tweet
        )
