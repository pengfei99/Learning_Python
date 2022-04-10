# from learning_python.Lesson04_Module_Package.src.pkg import mod1, mod2
__all__ = [
        'mod1',
        'mod2',
        'mod3',
        'mod4',
        'mod5'
        ]
print(f'Invoking __init__.py for {__name__}')
pkg_data = ['data', 'of', 'package']
