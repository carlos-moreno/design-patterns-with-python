class Singleton:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class SingletonLazyInstantiation:
    __instance = None

    def __init__(self):
        if not SingletonLazyInstantiation.__instance:
            print("__init__method called.")
        else:
            print(f"Instance already created: {self.getInstance()}")

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = SingletonLazyInstantiation()
        return cls.__instance


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


if __name__ == "__main__":
    s = Singleton()
    print(f"Object created ==> {s}")

    s1 = Singleton()
    print(f"Object created ==> {s1}")

    print("\n##### Singleton Lazy Instantiation #####")
    s_lazy = SingletonLazyInstantiation()
    print(f"Object created ==> {SingletonLazyInstantiation.getInstance()}")

    s1_lazy = SingletonLazyInstantiation()

    print("\n##### Meta Class Singleton #####")
    logger1 = Logger()
    logger2 = Logger()
    print(logger1, logger2)
