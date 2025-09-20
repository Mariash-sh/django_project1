from django import template
from cooking.models import Category


register = template.Library()

@register.simple_tag()
def get_all_categories():
    # кнопки категорий
    return Category.objects.all()