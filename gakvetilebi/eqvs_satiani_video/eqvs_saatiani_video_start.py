import random

dasawyisi      = 0
bolo           = 100
chafiqrebuli   = random.randint(dasawyisi, bolo)
print("chafiqrebuli ricxvis tipia = ",type(random.randint(dasawyisi, bolo)), "chafiqrebuli ricxvia ",chafiqrebuli)

while True:
    chasafiqrebeli = (input("sheiyvanet ricxvi: (or -> exit <- to exit the program) :"))
    if chasafiqrebeli.isdigit():
        print("Input is an integer!")
        chasafiqrebeli = int(chasafiqrebeli)

        if chasafiqrebeli == chafiqrebuli:
            print("tamashi moige!")
            break
        elif (chasafiqrebeli < chafiqrebuli):
            print("civa!")
        else:
            print("cxela!")
    elif chasafiqrebeli == "" or chasafiqrebeli == "exit":
        print("GAME OVER!")
        break
    else:
        print("Input is not an integer!")
        continue
