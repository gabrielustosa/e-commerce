from django.template import Library

register = Library()


@register.filter()
def format_price(value):
    if value == int(value):
        return f'R$ {value}'.replace('.', ',')
    return f'R$ {value:.2f}'.replace('.', ',')


@register.filter()
def range_list(value):
    return [v for v in range(value + 1)]
