class Cookie:
    def __init__(self):
        print(id(self))

a = Cookie()
b = Cookie()

def __repr__(self):
    return f'{id(self)}'

def __str__(self):
    return f' ** {id(self)}'
print(a)
print(b)
# <__main__.Cookie object at 0x10478d550>
# <__main__.Cookie object at 0x104998e10>

print(type(a))
print(type(b))
