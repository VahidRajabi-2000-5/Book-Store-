from django import template


register = template.Library()


@register.filter(name='to_lowercase_vahid')
# @register.filter()
def to_lowercase(value,ark):
    return f"{ark} : {value.lower()}"