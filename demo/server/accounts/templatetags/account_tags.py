from django import template
register = template.Library()


@register.inclusion_tag("avatar.html", takes_context=True)
def avatar(context, user=None, size=48):
    if not user:
        user = context['request'].user
    fullsize = f"{size}x{size}"
    return {
        'user': user,
        'fullsize': fullsize,
        'size': size
    }
