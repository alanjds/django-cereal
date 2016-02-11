import inspect

from celery.contrib.methods import task_method

from .pickle import DJANGO_CEREAL_PICKLE


class method_task(object):
    def __init__(self, app, **kwargs):
        self.app = app
        kwargs.setdefault('filter', task_method)
        kwargs.setdefault('serializer', DJANGO_CEREAL_PICKLE)
        self.kwargs = kwargs

    def __call__(self, method):
        module = inspect.getmodule(method)
        name = '{}.{}.{}'.format(module, method.__class__.__name__, method.__name__)
        return self.app.task.method_task(name=name, **self.kwargs)(method)
