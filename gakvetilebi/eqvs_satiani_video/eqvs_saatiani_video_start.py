import random
dasawyisi      = 0
bolo           = 100
chafiqrebuli   = random.randint(dasawyisi, bolo)
print("chafiqrebuli ricxvis tipia = ",type(random.randint(dasawyisi, bolo)), "chafiqrebuli ricxvia ",chafiqrebuli)

while True:
    chasafiqrebeli = int(input("sheiyvanet ricxvi: "))
    if chasafiqrebeli == chafiqrebuli:
        print("tamashi moige")
        break
    elif (chasafiqrebeli < chafiqrebuli):
        print("civa")
    else:
        print("cxela")
