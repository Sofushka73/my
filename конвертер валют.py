from ссылка import get_actual_currencies
# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 6. Подсчёт
# 7. Вывод результата

CURRENCIES = get_actual_currencies()

def convert(amount1, from_currency, to_currency, currencies):
    from_value = currencies.get(from_currency)
    to_value = currencies.get(to_currency)
    coefficient = to_value / from_value
    return round(amount1 * coefficient, 2)

# 1
print("Добро пожаловать в конвертатор валют!")

# 2
print("""
Инструкция:
1. Ввести исходную валюту
2. Ввести результирующую валюту
3. Ввести количество валюты
""")

print("Доступные валюты:")

for key in CURRENCIES['data']:
    print(f'* {key}')

# 3
current_currency = input('Введите исходную валюту: ').upper()
while not current_currency in CURRENCIES['data']:
    current_currency = input('Введите исходную валюту из списка: ').upper()

# 4
result_currency = input('Введите итоговую валюту: ').upper()
while not result_currency in CURRENCIES['data']:
    result_currency = input('Введите итоговую валюту из списка: ').upper()

# 5
amount = input("Введите количество: ")
while amount.isalpha():
    amount = input('Введите число: ')



# 6
result = convert(float(amount), current_currency, result_currency, CURRENCIES['data'])

print(f'{amount} {current_currency} = {result} {result_currency}')
