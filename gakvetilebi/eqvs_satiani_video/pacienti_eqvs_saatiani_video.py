pacientebi = ["gio","vaso","levaniko"]

print(pacientebi)
print("pacientebi type = ",type(pacientebi))

while True:
    print("exit the program -> exit <-")
    print("enter the name of new pacient: ")
    new_pacient = input("input -> the name of new pacient: ")

    if new_pacient == "" or new_pacient == "exit":
        break

    elif not new_pacient.isdigit() and not new_pacient in pacientebi:
        pacientebi.append(new_pacient)
        print(pacientebi)

    k = 0
    for new_pacient in pacientebi:
        print(new_pacient)
        print(k)
        k = k + 1



print("type of pacientebi[1] ", type(pacientebi[1]))
print("pacientebi[1] ", pacientebi[1])
print("pacientebi[1] ", pacientebi[1] + str(1))
