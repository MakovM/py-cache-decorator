from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def inner(*args, **kwargs) -> Callable:
        if args in cache:
            print("Getting from cache")
            return cache[args]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache[args] = result
        return result

    return inner
