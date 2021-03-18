

import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


# 템플릿 필터 만들기 |sub 빼기
@register.filter
def sub(value, arg):
    return value - arg

# 마크다운 필터
@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))