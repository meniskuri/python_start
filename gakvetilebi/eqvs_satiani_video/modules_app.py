import converters
from converters import kg_to_lbs
from converters import lbs_to_kg

x = converters.lbs_to_kg(12)
print("x = (lbs_to_kg(12)) ", x)

print("#######################")
print("lbs_to_kg (12)",lbs_to_kg(12))
print("kg_to_lbs (19)",kg_to_lbs(19))

y = converters.kg_to_lbs(19)
print("y = (kg_to_lbs(19)) ", y)
