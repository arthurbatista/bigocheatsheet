def fib(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    else:
        return fib(val - 1) + fib(val -2)

def fib_2(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    
    n1 = 1
    n2 = 2
    x = 3
    while x < val:
        t = n1
        n1 = n2
        n2 = n2 + t
        x += 1
    return n2

print(fib(4))
print(fib_2(4))
