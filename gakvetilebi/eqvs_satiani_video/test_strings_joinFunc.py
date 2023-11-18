import re
###
m = re.findall(r'\d+', "gio30")
print(m)
print(type(m))

pacientebi_chek = ["erti"]
pacientebi_chek[0] = "gio22"
k = re.search(r"\d+", pacientebi_chek[0])

x = "#".join(pacientebi_chek)
print("x = ", x)
print(type(x))


if k:
    print("Digit found at position", k.end())
    print("Digit found at position", k.start())

else:
    print("No digit in that string")


#p = '[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+'
p = '[\d]+'
s = x

if re.search(p, s) is not None:
    for catch in re.finditer(p, s):
        print(int(catch[0]) + 1) # catch is a match object
        print(type(catch[0]))

gio = "gio2"

print(gio + catch[0])
