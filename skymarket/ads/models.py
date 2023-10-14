from django.conf import settings
from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}
class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=150, verbose_name='название', **NULLABLE)
    image = models.ImageField(upload_to='Ad/', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='владелец', on_delete=models.CASCADE, **NULLABLE)
    price = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='стоимость')
    created_at = models.DateTimeField(auto_now_add=True, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.CharField(max_length=150, verbose_name='комментарий', default='')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='владелец', on_delete=models.CASCADE, **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, **NULLABLE)
    ad = models.ForeignKey(Ad, verbose_name='объявление', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
