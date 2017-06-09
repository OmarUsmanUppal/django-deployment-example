from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "Arg" from the string!
    """
    return cut.replace(arg,"")

# register.filter('cut',cut)#first one is the filter name we call, Second one is the function name
