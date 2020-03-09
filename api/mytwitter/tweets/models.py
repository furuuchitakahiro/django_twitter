from typing import ClassVar
from enum import Enum, unique

from django.db import models

from mytwitter.utils import generate_uniq_slug


@unique
class PublishStates(Enum):
    """

    """

    PRIVATE = ('private', 'プライベート')
    GLOBAL = ('global', 'グローバル')


class TweetManager(models.Manager):
    pass


class Tweet(models.Model):
    """

    """

    SLUG_LENGTH: ClassVar[str] = 10

    objects = TweetManager()

    slug = models.SlugField(
        # verbose_name='スラグ',
        max_length=SLUG_LENGTH,
        unique=True,
    )

    tweeter = models.ForeignKey(
        verbose_name='ツイート主',
        to='mytwitter_users.User',
        on_delete=models.CASCADE
    )
    body = models.TextField(verbose_name='本文')
    like = models.PositiveIntegerField(verbose_name='いいね', default=0)
    publish_state = models.CharField(
        max_length=10, choices=tuple(state.value for state in PublishStates)
    )

    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)

    def __str__(self) -> str:
        return self.slug

    @classmethod
    def _pre_save_handler(cls, sender, instance, raw, **kwargs):
        """保存直前処理

        """
        is_create: bool = instance.id is None

        # 作成時処理
        if is_create:
            if instance.slug == '' or instance.slug is None:
                instance.slug = generate_uniq_slug(
                    cls, 'slug', length=cls.SLUG_LENGTH
                )
