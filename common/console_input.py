name = input('id 입력하세요>>')

admin = 'choi'
user = 'park'

print(name)

pw = input('pw 입력하세요>>')
print(pw)

if name==admin:
    print('admin login')
elif name=='park' and len(pw)<5:
     print('user login')
else:
    print('not found user')


x=1
y=2

if x==1 and x>y:
    print('true')
elif x!=y and x==1:
    print('good')

