tickets_quantity = int(input("Сколько билетов хотите купить: "))

participants_age = [int(input('Введите возраст участников: ')) for i in range(tickets_quantity)]

sum_of_tickets = 0
average_price = 990
max_price = 1390
discount = 0.9

for i in participants_age:
    if 0 < i < 18:
        continue
    elif 18 <= i < 25:
        sum_of_tickets += average_price
    elif 25 <= i < 100:
        sum_of_tickets += max_price
    else:
        print(f'Возраст посетителя не может быть {i}')

if tickets_quantity > 3:
    sum_of_tickets = int(sum_of_tickets * 0.9)

print(sum_of_tickets)
