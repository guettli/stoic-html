from django.utils.html import mark_safe

from stoic_html import (
    join,
    list_to_html_list,
    link,
    admin_link, )


def test_join():
    assert join(['<', '>', '&'], ',') == '&lt;,&gt;,&amp;'
    assert join([1, 2, 3]) == '123'
    assert join([]) == ''
    assert join([], empty_text='x') == 'x'
    assert join(['x'], type='ul') == '<ul><li>x</li></ul>'
    assert join(['x'], type='ol') == '<ol><li>x</li></ol>'


def test_list_to_html_list():
    assert list_to_html_list(['a', 'b']) == '<ul><li>a</li><li>b</li></ul>'
    assert list_to_html_list(['a', 'b'], type='ol') == '<ol><li>a</li><li>b</li></ol>'
    assert list_to_html_list(['a', 'b'], type='ul') == '<ul><li>a</li><li>b</li></ul>'
    assert list_to_html_list([]) == ''


def test_link():

    class Dummy:
        def get_absolute_url(self):
            return 'x'

        def __str__(self):
            return 'y'

    assert link(Dummy()) == '<a href="x">y</a>'
    assert link(Dummy(), 1) == '<a href="x">1</a>'
    assert link(Dummy(), 'Peter & Mary') == '<a href="x">Peter &amp; Mary</a>'
    assert link(Dummy(), mark_safe('<button>press me</button>')) == '<a href="x"><button>press me</button></a>'


def test_admin_link():
    class Meta:
        app_label = 'auth'
        model_name = 'user'

    class DummyUser:
        id = 1
        def get_absolute_url(self):
            return '/foo'
        _meta = Meta()

        def __str__(self):
            return 'Dr. Foo'

    assert (
            admin_link(DummyUser()) == '<a href="/admin/auth/user/1/change/">Dr. Foo</a>'
    )
