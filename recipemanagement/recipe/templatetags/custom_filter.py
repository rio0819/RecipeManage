from django import template

register = template.Library()

@register.filter
def format_cook_time(value):
    if value:
        total_minutes = value.total_seconds() // 60
        return f"{int(total_minutes)}分"
    return "調理時間不明"