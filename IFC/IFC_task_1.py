import pandas as pd
import matplotlib.pyplot as plt
import os
import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
from pathlib import Path


model = ifcopenshell.open('./IFC/Example_1.ifc')

elements = model.by_type('ifcElement')
print(len(elements))
