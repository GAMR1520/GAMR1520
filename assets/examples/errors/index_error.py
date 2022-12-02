def b(arg):
    return a(arg).upper()

def a(arg):
    return arg[4]

data = "hello world".split()
c = b(data)