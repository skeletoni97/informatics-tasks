import ifcopenshell
import ifcopenshell.util.element

filepath = './IFC/Example_1.ifc'
model = ifcopenshell.open(filepath)

walls = model.by_type("IfcWall")

if len(walls) > 0:
    print(f"Количество стен в модели: {len(walls)}")
    first_wall = walls[0]

    psets = ifcopenshell.util.element.get_psets(first_wall)

    print("Полный словарь наборов свойств:")
    print(psets)

    print("\nПеречень Property Sets первой стены:")

    for pset_name, properties in psets.items():
        print(f"\nPset: {pset_name}")

        for property_name, property_value in properties.items():
            print(f"{property_name}: {property_value}")

else:
    print("В модели стены не найдены.")