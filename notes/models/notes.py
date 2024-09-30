from django.db import models
from django.contrib.auth import get_user_model


User =  get_user_model()


class Notes(models.Model):
    name = models.CharField('Название', max_length=255,)
    body = models.FileField('Файл', upload_to='uploads/%Y/%m',)
    owner =  models.ForeignKey(
        User, models.CASCADE, related_name='notes', verbose_name='Автор',
    )
    created_at = models.DateTimeField('Время создания', auto_now_add=True,)
    updated_at = models.DateTimeField('Последнее изменение', auto_now=True,)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return f'{self.name}'