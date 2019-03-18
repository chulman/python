from time import sleep

x=False

while x:
    sleep(1)
    print('a')


i=0

while i<3:
    print(i)
    i+=1

############## sequence
# 1.zip
days = 'monday', 'tuesday', 'wendsday'
french = 'a', 'b', 'c', 'd'

zip_list = list(zip(days, french))

print(zip_list)

# 2.range

for x in range(0, 3):
    print(x)


for x in range(2, -1, -1):
    print(x)


print(list(range(2010, 2016, 2)))

dicts = {"1":"asd"}
dicts.setdefault("defalut", "kkk")

print(dicts)

