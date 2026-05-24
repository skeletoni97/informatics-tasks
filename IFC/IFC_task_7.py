import ifcopenshell
import ifcopenshell.util.element
import shutil

filepath = './IFC/Example_1.ifc'

min_width = 900
output_filename = f"doors_wide_{min_width}.ifc"

# Создаем копию исходного IFC-файла
shutil.copy(filepath, output_filename)

# Открываем копию как подмодель
new_model = ifcopenshell.open(output_filename)

doors = new_model.by_type("IfcDoor")

# Удаляем двери, которые не подходят под условие
for door in doors:
    width = getattr(door, "OverallWidth", None)

    if width is None or width < min_width:
        new_model.remove(door)

# Сохраняем подмодель
new_model.write(output_filename)

# Проверяем результат
check_model = ifcopenshell.open(output_filename)
check_doors = check_model.by_type("IfcDoor")

print(f"Создан файл: {output_filename}")
print(f"Количество дверей в подмодели: {len(check_doors)}")

all_valid = True

for door in check_doors:
    width = getattr(door, "OverallWidth", None)

    if width is None or width < min_width:
        all_valid = False
        break

if all_valid:
    print(f"Проверка: все {len(check_doors)} дверей имеют ширину >= {min_width}")
else:
    print("Ошибка: найдены двери, не удовлетворяющие критерию")