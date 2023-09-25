from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="описание"
    )
    completed  = models.BooleanField(
        default=True, 
        verbose_name="статус выполнения"
    )
    created_at  = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания"
    )
    class Meta:
        verbose_name = "Основные настройки"
        verbose_name_plural = "Основная настройка"
