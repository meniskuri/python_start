import re
import time

pacientebi = ["gio","gio1","gio2"]
pacientebi_chek = ["erti"]
print(pacientebi)
print("pacientebi type = ",type(pacientebi))

print('''

ეს კოდი დასამთავრებელია.
გიო გიო1 გიო2 გიო3
და თუ შევიყვან გიო - ს ჩაამატოს ლისტში როგორც გიო4
თუ შევიყვან თეო - ს ჩაამატოს როგორც თეო და თუ კიდევ შევიყვან თეო - ს ჩაამატოს როგროც თეო1

მუშაობს !
''')

while True:

    k = 0

    for i in pacientebi:
        print("--------------------------------")
        print("k = ",k)
        print("i = ",i)
        print("pacientebi[k] = ",pacientebi[k])
        print("type(pacientebi[k]) = ",type(pacientebi[k]))
        print("pacientebi[k].isalpha() = ",pacientebi[k].isalpha())

        k = k + 1
        print("--------------------------------")

    print("exit the program -> exit <-")
    print("enter the name of new pacient: ")
    new_pacient = input("input -> the name of new pacient: ")

    if new_pacient == "" or new_pacient == "exit":
        break
    elif not new_pacient.isdigit() and not new_pacient in pacientebi:
        pacientebi.append(new_pacient)
        print("==================================")
        print(pacientebi)
        print("==================================")
    else:
        print(".......................................")
        pacientebi_chek[0] = new_pacient
        print("pacientebi_chek = ",pacientebi_chek)

        while pacientebi_chek[0] in pacientebi:
            m = re.search(r"\d", pacientebi_chek[0])

            if m:
                print("m = ",m)
                print("Digit found at end position", m.end())
                print("Digit found at start position", m.start())
                print("pacientebi_chek[0] = ", pacientebi_chek[0])
                print(type(m.start()))

                x = "#".join(pacientebi_chek)
                print("x = ", x)
                print(type(x))

                p = '[\d]+'
                s = x

                if re.search(p, s) is not None:
                    for catch in re.finditer(p, s):
                        print(int(catch[0]) + 1) # catch is a match object
                        print(type(catch[0]))


                print("x = ",x[:m.start()] + str(int(catch[0]) + 1))
                y = x[:m.start()] + str(int(catch[0]) + 1)
                print("y = ", y)

                pacientebi_chek[0] = y


                print("while shi var gachedili")
                time.sleep(2)


            else:
                print("No digit in that string",m)
                pacientebi_chek[0] = new_pacient + "1"

        pacientebi.append(pacientebi_chek[0])
        print("pacientebi = ",pacientebi)

        print(".......................................")
