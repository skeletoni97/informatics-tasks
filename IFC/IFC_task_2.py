import ifcopenshell

filepath = './IFC/Example_1.ifc'
model = ifcopenshell.open(filepath)

walls = model.by_type("IfcWall")

if len(walls) > 0:
    print(f"Количество стен в модели: {len(walls)}")
    first_wall = walls[0]

    print("Информация о первой стене:")
    print(f"  GlobalId: {first_wall.GlobalId}")
    print(f"  Name: {first_wall.Name}")
    print(f"  ObjectType: {first_wall.ObjectType}")
else:
    print("В модели стены не найдены.")