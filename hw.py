import inspect

def introspection_info(obj):
    
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    info['module'] = getattr(obj, '__module__', 'None')

    if inspect.isclass(obj) or hasattr(obj, '__class__'):
        info['base_classes'] = [base.__name__ for base in inspect.getmro(obj.__class__)]
    
    info['doc'] = inspect.getdoc(obj)

    return info

info = introspection_info(1)

print(info)
