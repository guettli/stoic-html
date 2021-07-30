# stoic-html

# What is "stoic-html"?

Stoic HTML is a tiny wrapper around the method [format_html()](https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.html.format_html) of the Django web framework.

Since I switched to developing the frontend with [htmx.org](//htmx.org) I tend to write small function-based-views returning small HTML fragments.

That's why I switched from using a template language to creating the HTML directly inside my Python code.

That's in general considered dirty, and frowned upon.

For me it is [Locality of Behaviour](https://htmx.org/essays/locality-of-behaviour/): I have all these things together in one place. That gives me a lot of power and speed.


# Install

```
python3 -m venv stoic-html-env
cd stoic-html-env/
. bin/activate
pip install -U pip wheel
pip install -e git+ssh://git@github.com/guettli/stoic-html.git#egg=stoic-html
cp src/stoic-html/.env.example src/stoic-html/.env
echo '. $VIRTUAL_ENV/src/stoic-html/.env' >> bin/activate
echo 'export $(cut -d= -f1 $VIRTUAL_ENV/src/stoic-html/.env)' >> bin/activate

. bin/activate

```

# Naming convention

See: https://github.com/guettli/django-htmx-fun

# Guidelines

See: https://github.com/guettli/programming-guidelines

