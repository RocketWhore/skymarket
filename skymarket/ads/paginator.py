from rest_framework.pagination import PageNumberPagination


class AdPaginator(PageNumberPagination):
    page_size = 4


class CommentPaginator(PageNumberPagination):
    page_size = 10
