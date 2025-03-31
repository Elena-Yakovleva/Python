# task
#
# Разработать приложение для определения знака зодиака по дате рождения.
# Пример:
#
# Введите месяц: март
# Введите число: 6
#
# Ваш знак зодиака: Рыбы

month = input( 'В каком месяце вы родились? ')
day = int(input('В какой день вы родились? '))

if month == 'март' and 21 <= day <= 31 or month == 'апрель' and 1 <= day <= 20:
  print('Ваш знак зодиака: Овен')
elif month == 'апрель' and 21 <= day <= 30 or month == 'май' and 1 <= day <= 21:
  print( 'Ваш знак зодиака: Телец')
elif month == 'май' and 22 <= day <= 31 or month == 'июнь' and 1 <= day <= 21:
  print( 'Ваш знак зодиака: Близнецы')
elif month == 'июнь' and 22 <= day <= 30 or month == 'июль' and 1 <= day <= 22:
  print( 'Ваш знак зодиака: Рак')
elif month == 'июль' and 23 <= day <= 31 or month == 'август' and 1 <= day <= 21:
  print( 'Ваш знак зодиака: Лев')
elif month == 'август' and 22 <= day <= 31 or month == 'сентябрь' and 1 <= day <= 23:
  print( 'Ваш знак зодиака: Дева')
elif month == 'сентябрь' and 24 <= day <= 30 or month == 'октябрь' and 1 <= day <= 23:
  print( 'Ваш знак зодиака: Весы')
elif month == 'октябрь' and 24 <= day <= 31 or month == 'ноябрь' and 1 <= day <= 22:
  print( 'Ваш знак зодиака: Скорпион')
elif month == 'ноябрь' and 23 <= day <= 30 or month == 'декабрь' and 1 <= day <= 22:
  print( 'Ваш знак зодиака: Стрелец')
elif month == 'декабрь' and 23 <= day <= 31 or month == 'январь' and 1 <= day <= 20:
  print( 'Ваш знак зодиака: Козерог')
elif month == 'январь' and 21 <= day <= 31 or month == 'февраль' and 1 <= day <= 19:
  print( 'Ваш знак зодиака: Водолей')
elif month == 'февраль' and 20 <= day <= 29 or month == 'март' and 1 <= day <= 20:
  print( 'Ваш знак зодиака: Рыбы')