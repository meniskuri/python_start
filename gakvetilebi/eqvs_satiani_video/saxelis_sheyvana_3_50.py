import time


chemisaxeli = input("sheiyvanet chemisaxeli: ")


while(True):
    print("chemisaxelia = ", chemisaxeli)

    if len(chemisaxeli) >= 3 and len(chemisaxeli) <= 50:
        print("length of name must be great than 3 and less then 50, name is good")
        break
    else:
        print("length of name must be great than 3 and less then 50, enter new name")
        chemisaxeli = input("sheiyvanet chemisaxeli: ")
