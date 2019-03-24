def func(a):
    return 'a' * 2


print(func(5))


def func(a, b):
    return a * b


print(func(1, 2))


# default parameter
def time(a=10, b=20):
    print(a, b)


time()
time(5, 15)


# 가변 파라미터
def var_parameter(*p):
    print(p)


var_parameter(1, 2, 3, 4, 5)


def var_parameter(**p):
    for key, values in p.items():
        print(key, values)


var_parameter(a=1, b=2)


# return - 파이썬은 다중 리턴이 가능하다. (튜플 형식으로 반환)

def multi_return(x, y):
    return y, x


a = multi_return(3, 5)
print(a)
print(type(a))  ## tuple
