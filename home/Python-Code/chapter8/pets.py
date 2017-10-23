def describe_pet(animal_type, pet_name):
    '''显示宠物的信息'''
    print("I have a "+ animal_type)
    print('my '+ animal_type +'\'s name is '+ pet_name)

describe_pet('hamster', 'harry')

# 關鍵字實參
describe_pet(pet_name='harry' , animal_type='hamster')

# 默認值 默認值要放最後
def describe_pet2(pet_name, animal_type='dog'):
    print("I have a " + animal_type)
    print('my '+ animal_type +'\'s name is '+ pet_name)

describe_pet2(pet_name='harry')

