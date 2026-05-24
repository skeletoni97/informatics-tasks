import ifcopenshell
from ifcopenshell.util.element import get_psets
filepath = './IFC/Example_1.ifc'
model = ifcopenshell.open(filepath)

walls = model.by_type("IfcWall")

# Выбираем первую стену
first_wall = walls[0]

# Выводим исходные свойства Name и ObjectType
print(f"Исходное Name: {first_wall.Name}")
print(f"Исходный ObjectType: {getattr(first_wall, 'ObjectType', None)}")

# Выводим исходное значение IsExternal из Pset_WallCommon
psets_before = get_psets(first_wall)
if "Pset_WallCommon" in psets_before and "IsExternal" in psets_before["Pset_WallCommon"]:
    print(f"Исходное IsExternal: {psets_before['Pset_WallCommon']['IsExternal']}")
else:
    print("IsExternal: не найден")
print("-" * 50)

# Изменяем значение свойства Name
first_wall.Name = "MODIFIED_" + (first_wall.Name if first_wall.Name else "Wall")
found = False
# Изменяем свойство IsExternal в Pset_WallCommon
for rel in first_wall.IsDefinedBy:
    if rel.is_a("IfcRelDefinesByProperties"):
        pset = rel.RelatingPropertyDefinition
        if pset.is_a("IfcPropertySet") and pset.Name == "Pset_WallCommon":
            for prop in pset.HasProperties:
                if prop.Name == "IsExternal":
                    # Меняем значение на противоположное
                    prop.NominalValue.wrappedValue = not prop.NominalValue.wrappedValue
                    found = True
                    break
            if not found:
                # Свойство не найдено
                print("Свойство IsExternal не найдено")    
            break

# Сохраняем измененную модель в новый файл
model.write("_modified.ifc")

# Заново открываем новый файл и проверяем изменения
new_model = ifcopenshell.open("_modified.ifc")
new_walls = new_model.by_type("IfcWall")
new_first_wall = new_walls[0]

print(f"Обновленное Name: {new_first_wall.Name}")

# Выводим измененное значение IsExternal
new_psets = get_psets(new_first_wall)
if "Pset_WallCommon" in new_psets and "IsExternal" in new_psets["Pset_WallCommon"]:
    print(f"Обновленное IsExternal: {new_psets['Pset_WallCommon']['IsExternal']}")