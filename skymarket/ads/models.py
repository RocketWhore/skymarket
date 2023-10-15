from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    image = models.ImageField(upload_to='Ad/', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    author = models.ForeignKey(User, verbose_name='владелец', on_delete=models.CASCADE, related_name='ads')
    price = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='стоимость')
    created_at = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'


class Comment(models.Model):
    text = models.CharField(max_length=150, verbose_name='комментарий', default='')
    author = models.ForeignKey(
        User, verbose_name='владелец', on_delete=models.CASCADE, related_name='comments'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, verbose_name='объявление', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
