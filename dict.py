user_profile = {
    'age': 20,
    'username': 'Yunaka',
    'weapons': ['Fists', 'Dagger'],
    'is_active': True,
    'clan': 'Papaya'
}

print(user_profile.keys())
user_profile['weapons'].append('Bow')
print(user_profile)
user_profile.update({'is_banned': False})
print(user_profile)
user_profile.update({'is_banned': True})
user2 = user_profile.copy()
user2.update({'username': 'NotYunaka', 'age': 21, 'clan': 'HiyaPapaya', 'is_banned': False})
print(user2)