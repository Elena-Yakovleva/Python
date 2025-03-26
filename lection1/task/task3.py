salary = input('Введите заработную плату в месяц: ')
mortgage = input('Введите, какой процент(%) уходит на ипотеку: ')
expenses = input('Введите, какой процент(%) уходит на жизнь: ')

salary_in_years = int(salary) * 12
mortgage_in_years = (int(salary) * int(mortgage) / 100 * 12)
expenses_in_years = (int(salary) * int(expenses) / 100 * 12)
accumulated = salary_in_years - mortgage_in_years - expenses_in_years

print('Вывод:')
print('На ипотеку было потрачено: ' + str(mortgage_in_years))
print('Было накоплено: ' + str(accumulated))