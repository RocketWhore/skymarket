from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer

from ads.permissions import IsAuthorOrAdmin

from ads.paginator import CommentPaginator, AdPaginator


class AdPagination(pagination.PageNumberPagination):
    pass


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = AdPaginator

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ('list', 'retrieve', 'create'):
            return super().get_permissions()
        permission_classes = (IsAuthorOrAdmin,)
        return [permission() for permission in permission_classes]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    pagination_class = CommentPaginator

    def perform_create(self, serializer):
        ad_id = self.kwargs.get('ad_id')
        ad = get_object_or_404(Ad, id=ad_id)
        serializer.save(author=self.request.user, ad=ad)

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_id')
        ad = get_object_or_404(Ad, id=ad_id)

        return ad.comments.all()

    def get_permissions(self):
        if self.action in ('list', 'retrieve', 'create'):
            return super().get_permissions()
        permission_classes = (IsAuthorOrAdmin,)
        return [permission() for permission in permission_classes]
