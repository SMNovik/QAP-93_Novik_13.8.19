visitors = {}  # Словарь (номер билета/посетителя : возраст)
price = []  # Список цен за билеты
price_1 = 0  # Стоимость билетов первого возрастного промежутка
price_2 = 990  # Стоимость билетов второго возрастного промежутка
price_3 = 1390  # Стоимость билетов третьего возрастного промежутка
total_cost = 0  # Итоговая суммарная стоимость билетов

#               Ввод количества билетов и исключение ошибок ввода
while True:
    try:
        num_of_ticket = int(input('Введите количество билетов - '))
        while num_of_ticket <= 0:
            num_of_ticket = int(input(f"Вы ошиблись. Введите правильное количество билетов : "))
        break
    except ValueError:
        print('Количество билетов является целым положительным числом')

#              Создание списка цен билетов в зависимости от возраста и исключение ошибок ввода
print('Цена билета зависит от возраста посетителя.')
for v in range(1, num_of_ticket + 1):
    while True:
        try:
            visitors[v] = int(input(f'Введите количество полных лет {v}го посетителя : '))
            while visitors.get(v) <= 0 or 110 < visitors.get(v):
                visitors[v] = int(input(f"Вы ошиблись. Введите правильный возраст {v} посетителя : "))
            break
        except ValueError:
            print('Количество полных лет является целым положительным числом')
    if 0 < visitors.get(v) < 18:
        price.append(price_1)
    elif 18 <= visitors.get(v) < 25:
        price.append(price_2)
    elif 25 <= visitors.get(v):
        price.append(price_3)
    print(f'Цена билета {v} посетилеля = ', price[v - 1])

#               Расчет общей стоимости билетов
if 3 < num_of_ticket:
    total_cost = sum(price) * 0.9
    print('Вы забронировали больше 3-х билетов.\nВаша скидка 10%')
    print('Сумма к оплате = ', total_cost)
else:
    total_cost = sum(price)
    print('Сумма к оплате = ', total_cost)
