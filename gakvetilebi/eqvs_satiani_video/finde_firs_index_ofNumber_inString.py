import re
s1 = "gio1"
m = re.search(r"\d", s1)
if m:
    print("Digit found at position", m.start())
    print(type(m.start()))
else:
    print("No digit in that string")
