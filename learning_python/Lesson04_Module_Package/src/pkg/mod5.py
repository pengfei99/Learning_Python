def show_global_var():
    from learning_python.Lesson04_Module_Package.src.pkg import pkg_data
    print(f"The global var imported from pkg: {pkg_data}")


def mod5_func():
    print('This is [mod5] function()')


class Mod5Class:
    pass
