from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager as _UserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from mytwitter.utils import generate_uniq_slug


class UserManager(_UserManager):
    """ユーザーマネージャー

    """
    pass


class User(AbstractBaseUser, PermissionsMixin):
    """ユーザー

    """

    SLUG_LENGTH = 20
    objects = UserManager()

    followee = models.ManyToManyField(to='User', related_name='followees')
    follower = models.ManyToManyField(to='User', related_name='followers')

    username = models.CharField(
        verbose_name=_('username'), max_length=150, blank=True
    )
    email = models.EmailField(_('email address'), unique=True)
    slug = models.CharField(
        verbose_name=_('slug'),
        unique=True,
        max_length=SLUG_LENGTH
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

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
