# Generated by Django 3.0.3 on 2020-02-26 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=10, unique=True, verbose_name='スラグ')),
                ('body', models.TextField(verbose_name='本文')),
                ('like', models.PositiveIntegerField(default=0, verbose_name='いいね')),
                ('publish_state', models.CharField(choices=[('private', 'プライベート'), ('global', 'グローバル')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('tweeter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ツイート主')),
            ],
        ),
    ]
