import ifcopenshell

filepath = './IFC/Example_1.ifc'
model = ifcopenshell.open(filepath)

elements = model.by_type('ifcElement')
print(len(elements))
walls = model.by_type("IfcWall")
print(f"Количество стен в модели: {len(walls)}")