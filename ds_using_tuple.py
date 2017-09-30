zoo = ('python', 'elephant', 'penguin')
print('num of the zoo is', len(zoo))
new_zoo = 'monkey', 'dog', zoo

print('num of the cage of new zoo is', len(new_zoo))
print('all animals in the new zoo are', new_zoo)
print('animals brought from the old zoo are', new_zoo[2])
print('last animal of the old zoo is', new_zoo[2][2])

print('num of the animals in the new zoo is',

      len(new_zoo)-1+len(new_zoo[2]))