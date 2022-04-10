def show_global_var():
    from learning_python.Lesson04_Module_Package.src.pkg import pkg_data
    print(f"The global var imported from pkg: {pkg_data}")


def mod3_func():
    print('This is [mod3] function()')


class Mod3Class:
    pass
