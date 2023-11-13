import re


myList = ["gio1"]
print(type(myList))


m = re.search(r"\d", myList[0])
if m:
    print("Digit found at position", m.start())
    print(type(m.start()))
else:
    print("No digit in that string")


x = "#".join(myList)

print(x)
print(x[:3])
print(type(x))
