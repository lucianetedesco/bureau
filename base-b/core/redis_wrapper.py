from functools import wraps

from core.redis import RedisClient


def cache():
    def cache(fn):
        @wraps(fn)
        def wrapper(self_origin, *args, **kwargs):
            class_name = self_origin.__class__.__name__
            function = fn.__name__
            args_string = ''.join(args)
            key = f'{class_name}.{function}.{args_string}'

            on_cache = RedisClient().get(key)
            if on_cache:
                return on_cache

            func_return = fn(self_origin, *args, **kwargs)

            RedisClient().set(key, func_return)

            return func_return

        return wrapper

    return cache
