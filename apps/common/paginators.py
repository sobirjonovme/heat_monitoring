from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                "page": self.get_page_number(self.request, self.page.paginator),
                "count": self.page.paginator.count,
                "page_size": self.get_page_size(self.request),
                "results": data,
            }
        )
