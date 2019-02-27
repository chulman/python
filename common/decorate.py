
def decorate(func):
    def func_wrapper():
        print('welcome to')
        func()
        print('test2')


@decorate
def func():
    print('hello world')


func()