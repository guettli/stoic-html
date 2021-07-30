from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import conditional_escape
from django.utils.html import format_html
from django.utils.safestring import mark_safe


def join(my_list, sep='', type=None, empty_text=''):
    if not my_list:
        return empty_text
    if type is None:
        return mark_safe(sep.join([conditional_escape(item) for item in my_list]))
    if type == 'ul':
        return format_html(
            '<ul>{}</ul>', join([format_html('<li>{}</li>', item) for item in my_list])
        )
    raise Exception(f'Unknown type {type}')


def link(obj):
    if isinstance(obj, User):
        url = reverse('user_profile_page', kwargs=dict(user_id=obj.id))
    else:
        url = obj.get_absolute_url()
    return format_html('<a href="{}">{}</a>', url, obj)


def list_to_html_list(items, type='ul', li_style=''):
    new = []
    if li_style:
        li_style = format_html(' style="{li_style}"', li_style=li_style)
    for item in items:
        item = item.strip()
        if not item:
            continue
        new.append(
            format_html('<li{li_style}>{item}</li>', li_style=li_style, item=item)
        )
    if not new:
        return ''
    return format_html('<{type}>{items}</{type}>', type=type, items=join(new))


def admin_link(obj, text=None):
    if obj is None:
        return ''
    if text is None:
        text = str(obj)
    return format_html(
        '<a href="{}">{}</a>',
        reverse(
            f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', args=(obj.id,)
        ),
        text,
    )
