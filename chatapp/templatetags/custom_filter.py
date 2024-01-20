from django import template

register=template.Library()

@register.filter(name='my_custom_filter')
def if_id_in_queryset(id,queryset):
    return any (id==query.receiver.id for query in queryset)