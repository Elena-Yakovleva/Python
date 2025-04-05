boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']



list = zip(sorted(boys), sorted(girls))
if len(boys) == len(girls):
    print('Идеальные пары:')
    for boy, girl in list:
        print(boy, 'и', girl)
elif len(boys) > len(girls):
    x = len(boys) - len(girls)
    print(f'Внимание! Не хватает девушек. Необходимо добавить {x}   девушек ')

else:
    y = len(girls) - len(boys)
    print(f'Внимание! Не хватает парней. Необходимо добавить {y}   девушек ')