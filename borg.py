class Borg:
    _share_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._share_state
        return obj


if __name__ == '__main__':
    b = Borg()
    b1 = Borg()
    b.x = 4
    b1.y = 10

    print(f'Borg Object b: {b}')
    print(f'Borg Object b1: {b1}')
    print(f'Object State b: {b.__dict__}')
    print(f'Object State b1: {b1.__dict__}')
