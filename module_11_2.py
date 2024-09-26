import inspect
from pprint import pprint


def introspection_info(obj):
    result = {}
    result['type'] = type(obj)
    result['attributes'] = dir(obj)
    result['methods'] = [method for method in dir(type(obj)) if callable(getattr(obj, method))]
    result['module'] = inspect.getmodule(introspection_info)
    return result


number_info = introspection_info(42)
pprint(number_info)
