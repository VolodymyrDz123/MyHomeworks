"""
Task 2. Є два довільних числа які відповідають за мінімальну і максимальну ціну.
Є Dict з назвами магазинів і цінами:
{ "cilpio": 47.999, "a_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.ua": 38.324,
"my-store": 37.166, "the_partner": 38.988, "sto": 37.720, "rozetka": 38.003}.
Напишіть код, який знайде і виведе на екран назви магазинів,
ціни яких попадають в діапазон між мінімальною і максимальною ціною. Наприклад:
lower_limit = 35.9
upper_limit = 37.339
> match: "my-store", "main-service"
"""

shop_price = {
    "cilpio": 47.999,
    "a_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.ua": 38.324,
    "my-store": 37.166,
    "the_partner": 38.988,
    "sto": 37.720,
    "rozetka": 38.003,
}
shops_selected_range = []
try:
    min_price = float(input("Вкажіть мінімальну ціну: "))
    max_price = float(input("Вкажіть максимальну ціну: "))
except ValueError as e:
    print("Значення має бути в цифрах")
else:
    if max_price < min_price:
        print("Максимальне значення не може бути меншим за мінімальне")
    else:
        for shop, price in shop_price.items():
            if price >= min_price and price <= max_price:
                shops_selected_range.append(shop)
        if shops_selected_range:
            print(f"Назви магазинів з ціною у вибраному діапазоні {shops_selected_range}")
        else:
            print("Немає магазинів з ціною у вибраному діапазоні")
