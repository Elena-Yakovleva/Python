
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


ids1 = ids['user1']
ids2 = ids['user2']
ids3 = ids['user3']

new_ids = set(ids1 + ids2 + ids3)
new_ids = list(new_ids)

print(new_ids)

