
pot={}
def foo():
    global pot
    pot={"a":1}
    print(pot)


def bar():
    print(pot)

foo()
bar()
