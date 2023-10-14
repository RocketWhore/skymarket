from rest_framework import pagination, viewsets


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
    permission_classes = [IsAuthorOrAdmin]
    pagination_class = [AdPaginator]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def get_queryset(self):
    if self.request.user.groups.filter(name='moderator').exists():
        return Ad.objects.all()

    return Ad.objects.filter(user=self.request.user)


# def get_permissions(self):
#     permission_classes = (IsAuthenticated,)
#
#     if self.action == 'create':
#         permission_classes = (IsModerator,)
#
#     elif self.action == 'destroy':
#         permission_classes = (IsModerator, IsUserOrStaff)
#
#     elif self.action == 'update' or self.action == 'partial_update':
#         permission_classes = (IsModerator | IsUserOrStaff,)
#
#     return [permission() for permission in permission_classes]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthorOrAdmin]

    pagination_class = [CommentPaginator]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def get_queryset(self):
    if self.request.user.groups.filter(name='admin').exists():
        return Comment.objects.all()

    return Comment.objects.filter(user=self.request.user)

