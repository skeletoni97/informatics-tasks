materials = {
    "бетон": 5200,
    "кирпич": 18,
    "цемент": 430,
    "арматура": 61000,
    "песок": 900
}

materials["щебень"] = 1200
materials["гипс"] = 350
materials["цемент"] *= 1.10
del materials["песок"]
average_price = sum(materials.values()) / len(materials)

print("Прайс-лист материалов:")
for material, price in materials.items():
    print(f"{material}: {price:.2f} руб.")

print(f"\nСредняя цена: {average_price:.2f} руб.")