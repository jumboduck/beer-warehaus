from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    """
    # The following tag ensures url parameters
    # are kept when using pagination links.
    """
    query = context['request'].GET.copy()
    query.update(kwargs)
    return query.urlencode()
