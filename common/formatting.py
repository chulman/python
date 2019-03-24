# String interpolation

city = 'anyang'
nation = 'korea'

print('{} {}'.format(city, nation))
print('{1} {0}'.format(city, nation))
print('{city} {nation}'.format(city='seoul', nation='kr'))

dict = {'name': 'chulman', 'city': 'anyang', 'nation': 'kr'}

print('{0[name]} {0[city]} {0[nation]}'.format(dict))
