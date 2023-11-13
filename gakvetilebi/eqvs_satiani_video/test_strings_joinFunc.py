import re


myList = ["gio"]
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
print(int(x[m.start()])+1)
print(type(x[m.start()]))
