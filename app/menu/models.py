from django.db import models


class Menu(models.Model):
    """Модель меню."""
    
    title = models.CharField(max_length=255, verbose_name='Название меню')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ('title',)


class Item(models.Model):
    """Модель, описывающая пункт древовидного меню."""

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Меню', related_name='items')
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Родительский элемент',
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ('title',)