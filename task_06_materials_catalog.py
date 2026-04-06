materials = ["бетон", "кирпич", "цемент", "арматура", "песок"]

first_material = materials[0]
last_material = materials[-1]
middle_materials = materials[1:-1]

materials.append("щебень")
materials.append("гипс")

materials.pop(1)

print(
    f"Первый материал: {first_material}\n"
    f"Последний материал: {last_material}\n"
    f"Средние элементы: {middle_materials}\n"
    f"Итоговый список: {materials}\n"
    f"Длина списка: {len(materials)}"
)