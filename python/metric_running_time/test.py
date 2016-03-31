from fn_timer import fn_timer

@fn_timer
def foo():
    for i in range(100000000):
        count = i
foo()
