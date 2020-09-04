def singleton(myClass):
    instances = {}

    def getInstance(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]

    return getInstance


@singleton
class Teste:
    def __init__(self):
        self.x = 10


if __name__ == "__main__":
    x = Teste()
    x1 = Teste()
    x2 = Teste()
    print(f"Object x is {x}")
    print(f"Object x1 is {x1}")
    print(f"Object x2 is {x2}")
