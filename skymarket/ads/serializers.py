from rest_framework import serializers

from ads.models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'created_at', 'ad')
        read_only_fields = ('id', 'author', 'created_at', 'ad')


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ('id', 'title', 'image', 'description', 'price', 'created_at', 'author')
        read_only_fields = ('id', 'author', 'created_at')



