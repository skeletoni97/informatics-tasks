import pandas as pd
import matplotlib.pyplot as plt
import os
import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
from pathlib import Path

filepath = './IFC/Example_1.ifc'
model = ifcopenshell.open(filepath)

elements = model.by_type('ifcElement')
print(len(elements))
walls = model.by_type("IfcWall")
print(f"Количество стен в модели: {len(walls)}")