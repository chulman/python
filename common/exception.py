class TestException(Exception):
    pass


###예외 잡기
try:
    f = open('isFile.txt', 'r')
    print(f.read())
except FileNotFoundError:
    print('file is not exist')

try:
    f = open('isFile.txt', 'r')
    print(f.read())
except FileNotFoundError as err:
    print('{}'.format(err))
except:
    print('remain except')




## 예외 발생

try:
    f = open('isFile.txt', 'r')

except FileNotFoundError as err:
    raise TestException('test')
    print(err)