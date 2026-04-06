def calculate_discount(price, quantity):
    total_cost = price * quantity

    if total_cost < 1000:
        discount = 0
    elif total_cost <= 5000:
        discount = 5
    else:
        discount = 10

    discount_amount = total_cost * discount / 100
    final_cost = total_cost - discount_amount

    return (
        f"Цена товара: {price:.2f} руб.\n"
        f"Количество товара: {quantity}\n"
        f"Стоимость без скидки: {total_cost:.2f} руб.\n"
        f"Скидка: {discount}%\n"
        f"Сумма скидки: {discount_amount:.2f} руб.\n"
        f"Итоговая стоимость: {final_cost:.2f} руб."
    )

price = float(input("Введите цену товара: "))
quantity = int(input("Введите количество товара: "))

print(calculate_discount(price, quantity))