from typing import Type
import secrets

from django.db.models import Model


def generate_uniq_slug(
    model_class: Type[Model],
    field_name: str = 'slug',
    length: int = 50,
    prefix: str = '',
    sufix: str = ''
) -> str:
    """ユニークなスラグを生成

    Args:
        model_class (Type['django.db.models.Model']): モデルクラス
        field_name (str): スラグのフィールド名 ( default 'slug' )
        length (int): スラグの長さ ( default 50 )
        prefix (str): スラグに付与するプレフィックス
        sufix (str): スラグに付与するサフィックス

    Returns:
        str: ユニークなスラグ

    """
    slug = f'{prefix}{secrets.token_hex(length)[0:length]}{sufix}'
    query_args = {
        field_name: slug
    }
    qs_exists = model_class.objects.filter(**query_args).exists()

    # スラグがかぶっていたら作り直して検証する
    while(qs_exists):
        slug = f'{prefix}{secrets.token_hex(length)[0:length]}{sufix}'
        qs_exists = model_class.objects.filter(**{
            field_name: slug
        }).exists()

    return slug
