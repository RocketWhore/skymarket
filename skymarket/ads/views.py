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
    permission_classes = (IsAuthenticated,)
    pagination_class = AdPaginator

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # if self.request.user.groups.filter(name='moderator').exists():
        #     return Ad.objects.all()

        return Ad.objects.filter(author=self.request.user)

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return super().get_permissions()
        permission_classes = (IsAuthorOrAdmin,)
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['GET'], serializer_class=CommentSerializer)
    def comments(self, *args, **kwargs):
        comments = self.get_object().comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthorOrAdmin]

    pagination_class = CommentPaginator

    def perform_create(self, serializer):
        ad_id = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, id=ad_id)
        serializer.save(author=self.request.user, ad=ad)

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, id=ad_id)
        if self.request.user.groups.filter(name='admin').exists():
            return Comment.objects.all()

        return Comment.objects.filter(author=self.request.user, ad=ad)

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return super().get_permissions()
        permission_classes = (IsAuthorOrAdmin,)
        return [permission() for permission in permission_classes]
