import re
###
new_pacient = input("input -> the name of new pacient: ")

pacientebi_chek = ["erti"]
pacientebi_chek[0] = new_pacient

x = "#".join(pacientebi_chek)
print("x = ", x)
print(type(x))


k = re.search(r"\d+", pacientebi_chek[0])
if k:
    print("Digit found at position", k.start())
    print("Digit found at position", k.end())
else:
    print("No digit in that string")


#p = '[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+'
p = '[\d]+'
s = x

if re.search(p, s) is not None:
    for catch in re.finditer(p, s):
        print(int(catch[0]) + 1) # catch is a match object
        print(type(catch[0]))


print("x = ",x[:k.start()] + str(int(catch[0]) + 1))
print(type(x))
