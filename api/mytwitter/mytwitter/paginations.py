from rest_framework import pagination
from rest_framework.response import Response


class MyTwitterPagination(pagination.PageNumberPagination):
    """ページャー

    """
    page_size_query_param = 'limit'
    page_size = 10
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'limit': self.get_page_size(self.request),
            'current': self.page.number,
            'count': self.page.paginator.count,
            'results': data
        })
