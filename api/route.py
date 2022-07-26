routes = {}


class Route:

    def __init__(self, path=None):

        self.path = path


    def __call__(self, func):

        if not self.path:
            self.path = "/" + func.__name__

        routes.setdefault(self.path, func)

        def call(*args, **kwargs):
            return func(*args, **kwargs)

        return call
