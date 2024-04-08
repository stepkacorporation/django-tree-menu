from django import template
from django.db.models.query import QuerySet
from django.template.context import RequestContext

from ..models import Item

register = template.Library()


@register.inclusion_tag(filename='menu/menu.html', takes_context=True)
def draw_menu(context: RequestContext, menu: str):
    """
    Формирует контекстный словарь на основе указанного имени
    меню для передачи в шаблон menu.html.
    
    Args:
        - context (RequestContext): Контекст запроса Django.
        - menu (str): Название меню, для которого следует отобразить элементы.

    Returns:
        - dict: Словарь контекста для шаблона, содержащий элементы меню и название меню.
    """
    
    items = Item.objects.filter(menu__title=menu)
    items_values = items.values()
    main_parents: list[dict] = [item for item in items_values.filter(parent=None)]

    result_context = {'items': main_parents, 'menu': menu}

    slug = context['request'].GET.get(menu)
    if not slug:
        return result_context
    
    try:
        selected_item = items.get(slug=slug)
    except Item.DoesNotExist:
        return result_context

    external_items = get_external_items_id_list(selected_item)
    for parent in main_parents:
        if parent['id'] in external_items:
            parent['children'] = get_child_items(items_values, parent['id'], external_items)

    return result_context


def get_external_items_id_list(parent: Item):
    """
    Возвращает список идентификаторов внешних элементов, начиная с
    указанного родительского элемента.

    Args:
        - parent (Item): Родительский элемент.

    Returns:
        - list[int]: Список идентификаторов внешних элементов.
    """

    id_list = []
    while parent:
        id_list.append(parent.id)
        parent = parent.parent

    return id_list


def get_child_items(items_values: QuerySet, parent_id: int, external_items: list[int]) -> QuerySet:
    """
    Возвращает дочерние элементы для указанного родительского элемента.

    Аргументы:
        - items_values (QuerySet): QuerySet, содержащий значения элементов меню.
        - parent_id (int): Идентификатор родительского элемента.
        - external_items (list[int]): Список идентификаторов внешних элементов.

    Возвращает:
        - QuerySet: Дочерние элементы для указанного родительского элемента.
    """

    child_items = items_values.filter(parent_id=parent_id)
    for child in child_items:
        if child['id'] in external_items:
            child['children'] = get_child_items(items_values, child['id'], external_items)
    
    return child_items