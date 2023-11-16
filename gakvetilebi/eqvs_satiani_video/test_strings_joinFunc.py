import re
m = re.findall(r'\d+', "gio30")
print(m)
print(type(m))

pacientebi_chek = ["erti"]
pacientebi_chek[0] = "gio10"
k = re.search(r"\d+", pacientebi_chek[0])
if k:
    print("Digit found at position", k.end())
    print("Digit found at position", k.start())
    print(type(k.end()))
    
else:
    print("No digit in that string")
