def user_info(first, last, **other_info):
    profile={}
    profile['first name']= first
    profile['last name']= last

    for key,value in other_info.items():
        profile[key] = value
    return profile

user_profile = user_info('hello','world',location='wuhan',address='nowhere')

print(user_profile)
