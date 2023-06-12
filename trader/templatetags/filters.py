from django import template

register = template.Library()

@register.filter
def remove_spaces(value):
    return value.replace(" ","")

@register.filter
def attr_class(field, css_class):
    return field.as_widget(attrs={"class":css_class})

@register.filter
def attr_placeholder(field, placeholder):
    return field.as_widget(attrs={"placeholder":placeholder})

@register.filter
def underscore(value):
    return value.replace(" ","_")