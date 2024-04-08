from django.contrib import admin

from .models import Menu, Item

    
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Админ-панель меню."""

    list_display = ('id', 'title',)
    search_fields = ('title',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Админ-панель элемента древовидного меню."""

    list_display = ('title', 'slug', 'parent', 'menu')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    autocomplete_fields = ('menu', 'parent')
    fieldsets = (
        (None, {
            'fields': ('menu', 'parent', 'title', 'slug'),
        }),
    )
