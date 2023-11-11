import re

pacientebi = ["gio","gio1","gio2"]
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

        m = re.search(r"\d", pacientebi[k])
        if m:
            print("Digit found at position", m.start())
            print(type(m.start()))
        else:
            print("No digit in that string")


        k = k + 1
        print("--------------------------------")


    print("exit the program -> exit <-")
    print("enter the name of new pacient: ")
    new_pacient = input("input -> the name of new pacient: ")

    if new_pacient == "" or new_pacient == "exit":
        break
    elif not new_pacient.isdigit():
        # pacientebi.append(new_pacient)
        print("==================================")
        print(pacientebi)
        print("==================================")


print("type of pacientebi[1] ", type(pacientebi[1]))
print("pacientebi[1] ", pacientebi[1])
print("pacientebi[1] ", pacientebi[1] + str(1))
