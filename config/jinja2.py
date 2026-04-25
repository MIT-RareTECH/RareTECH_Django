from django.templatetags.static import static
from django.urls import reverse
from django.middleware.csrf import get_token
from jinja2 import Environment
from markupsafe import Markup


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
    })

    #csrf_inputを{{ csrf_input }}で使えるようにする
    def csrf_input(request):
        return Markup(f'<input type="hidden" name="csrfmiddlewaretoken" value="{get_token(request)}">')

    env.globals['csrf_input'] = property(csrf_input)    
    return env

