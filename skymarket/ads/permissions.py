# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrAdmin(BasePermission):

    # def has_permission(self, request, view):
    #     if request.user.is_staff:
    #         return True
    #
    #     return request.user == view.get_object().author
    #
    def has_object_permission(self, request, view, obj):
        return (
                request.method in SAFE_METHODS
                or (request.user == obj.author)
                or request.user.is_staff
        )
