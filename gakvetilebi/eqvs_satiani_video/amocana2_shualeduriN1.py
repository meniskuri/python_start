print("ამოცანა N2. შექმენით სიტყვაში ასოების გამამრავლებელი პროგრამა:")

def asoebisgamravleba2ze(sityva, ricxvi):
    gamotana = []

    for i in sityva:

        gamotana.append(i*ricxvi)
        print("i ras udris? = ", i)
        print(type(gamotana))
        gamotana2 = "".join(gamotana)
        print(type(gamotana2))

    return eval("print(gamotana2)")


sityva = input("sheitanet nebismieri sityva: ")

# aq unda shemyavdes marto ricxvi - whil it gavaketo

while True:
    ricxvi = input("sheitanet nebismieri mteli ricxvi: ")
    if ricxvi.isdigit():
        ricxvi = int(ricxvi)
        break
    else:
        print("sheitanet nebismieri mteli ricxvi (sheyvanili ar aris mteli ricxvi): ")


asoebisgamravleba2ze(sityva, ricxvi)

#ricxvi = int(input("sheitanet nebismieri mteli ricxvi: "))
