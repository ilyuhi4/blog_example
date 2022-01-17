from django import template

from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    """Function name in template tags name
       To use it you need to {% load %} in template
    """
    return Post.published.count()