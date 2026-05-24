import ifcopenshell
import ifcopenshell.util.element

filepath = './IFC/Example_1.ifc'
model = ifcopenshell.open(filepath)

doors = model.by_type("IfcDoor")

min_width = 900 # (в мм)

# Список для «узких» дверей
narrow_doors = []

# Проходим по всем дверям
for door in doors:
    name = door.Name
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)
    
    # Если ширина задана и меньше порога, добавляем в список
    if width is not None and width < min_width:
        narrow_doors.append((name, width, height))

# Выводим информацию о «узких» дверях
for name, width, height in narrow_doors:
    print(f"{name}: ширина = {round(width, 3)}, высота = {round(height, 3) if height else None}")

# Выводим количество найденных узких дверей или сообщение об отсутствии
if narrow_doors:
    print(f"Количество узких дверей: {len(narrow_doors)}")
else:
    print("Узких дверей не обнаружено")