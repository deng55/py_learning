ab = {
    'tom':'tom@gmail.com',
    'jack':'jack@gmail.com',
    'henry':'henry@gmail.com',
    'ed':'ed@gmail.com'
}

print('tom\'s email is',ab['tom'])

del ab['tom']

print('ab is',ab)
print(len(ab))

print('there are {} contacts in the address-book'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name,address))

ab['lucy'] = 'lucy@gmail.com'

if 'lucy' in ab:
    print('lucy\'s address is ', ab['lucy'])

print(ab.pop('lucy'))