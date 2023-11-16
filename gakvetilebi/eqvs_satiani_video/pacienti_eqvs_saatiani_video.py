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
თავს ვერ ვაბავ ჯერ

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

        #m = re.search(r"\d", pacientebi[k])
        #if m:
        #    print("Digit found at position", m.start())
        #    print(type(m.start()))
        #else:
        #    print("No digit in that string")
        #
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
                print("Digit found at position", m.start())
                print(type(m.start()))
            else:
                print("No digit in that string")

            print("while shi var gachedili")
            time.sleep(2)


            x = "#".join(pacientebi_chek)
            print("x = ", x)
            print("x[int(m.start())] = ",x[int(m.start())])

            print("000000000000000000000")
            y = x.replace(x[int(m.start())], str(int(x[m.start()])+1))
            print(" y = ",y)
            print("000000000000000000000")


            pacientebi_chek[0] = y
            print("pacientebi_chek = ",pacientebi_chek)
        pacientebi.append(pacientebi_chek[0])

        print(".......................................")
