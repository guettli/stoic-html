from stoic_html import (
    join,
    list_to_html_list,
    link,
    admin_link, )


def test_join():
    assert 0
    assert join(['<', '>', '&'], ',') == '&lt;,&gt;,&amp;'
    assert join([1, 2, 3]) == '123'
    assert join([]) == ''
    assert join([], empty_text='x') == 'x'


def test_list_to_html_list():
    assert list_to_html_list(['a', 'b']) == '<ul><li>a</li><li>b</li></ul>'
    assert list_to_html_list(['a', 'b'], type='ol') == '<ol><li>a</li><li>b</li></ol>'
    assert list_to_html_list([]) == ''


def test_link():

    class Dummy:
        def get_absolute_url(self):
            return 'x'

        def __str__(self):
            return 'y'

    assert link(Dummy()) == '<a href="x">y</a>'


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
