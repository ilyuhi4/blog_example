from django import template

from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    """Function name in template tags name
       To use it you need to {% load %} in template
    """
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by(field_names='-publish')[:count]
    return {'latest_posts': latest_posts}