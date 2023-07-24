from learning_python import __version__
from learning_python.Lesson14_Desgin_Pattern.Singleton.MySingleton import MySingletonMeta


def test_version():
    assert __version__ == '0.1.0'


def test_MySingleton_is_always_same_object():
    """
    This needs to be revisited, it does not work
    :return:
    :rtype:
    """
    assert MySingletonMeta() is MySingletonMeta()

    # Sanity check - a non-singleton class should create two separate
    #  instances
    class NonSingleton:
        pass

    assert NonSingleton() is not NonSingleton()
