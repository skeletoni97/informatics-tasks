warehouse = {
 "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
 "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
 "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
 "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
 "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}

print("=" * 50)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 50)
print("Материал | Кол-во |   Цена   | Мин. | Стоимость")
print("-" * 50)

total_cost = 0
critical_materials = []

for material, data in warehouse.items():
    # Стоимость конкретного материала = количество * цена
    cost = data["quantity"] * data["price"]
    total_cost += cost

    critical_mark = ""

    # Проверка на критический остаток
    if data["quantity"] < data["min_quantity"]:
        critical_mark = " ⚠ КРИТИЧ!"
        critical_materials.append(material)

    print(
        f"{material:<8} | "
        f"{data['quantity']:<6} | "
        f"{data['price']:<8} | "
        f"{data['min_quantity']:<4} | "
        f"{cost:.2f}{critical_mark}"
    )

print("=" * 50)
print(f"ОБЩАЯ СТОИМОСТЬ: {total_cost:.2f} руб")


# Поиск самого дорогого материала по цене за единицу
most_expensive = max(warehouse, key=lambda material: warehouse[material]["price"])
print(warehouse[most_expensive]["price"])
max_price = warehouse[most_expensive]["price"] * warehouse[most_expensive]["quantity"]
print(f"Самый дорогой: {most_expensive} ({max_price} руб)")

# Вывод списка материалов с критическим остатком
print(f"⚠ КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_materials)}):")
for material in critical_materials:
    print(f"- {material}: {warehouse[material]['quantity']} < {warehouse[material]['min_quantity']}")




print("=== ВЫДАЧА МАТЕРИАЛА ===")
material_name = input("Введите материал: ").strip().capitalize()
# Проверка наличия материала на складе
if material_name in warehouse:
    issue_quantity = int(input("Введите количество: "))

    # Проверка, хватает ли количества для выдачи
    if warehouse[material_name]["quantity"] >= issue_quantity:
        old_quantity = warehouse[material_name]["quantity"]
        warehouse[material_name]["quantity"] -= issue_quantity
        new_quantity = warehouse[material_name]["quantity"]

        print(f"✓ Выдано {issue_quantity} единиц '{material_name}'")
        print(f"Остаток: {old_quantity} -> {new_quantity}")
    else:
        print("Недостаточно материала на складе")
else:
    print("Материал не найден")