import ifcopenshell
import ifcopenshell.util.element

filepath = './IFC/Example_1.ifc'
model = ifcopenshell.open(filepath)

storeys = model.by_type("IfcBuildingStorey")

print(f"IFC schema: {model.schema}")
print(f"Количество этажей: {len(storeys)}")

for storey in storeys:
    name = storey.Name
    elevation = storey.Elevation if storey.Elevation is not None else None
    print(f"Этаж: {name}, Elevation={elevation}")

