from django import template

register = template.Library()

@register.filter
def confidence_percent(value):
    try:
        return "{:.2f}".format(float(value) * 100)
    except:
        return "0.00"