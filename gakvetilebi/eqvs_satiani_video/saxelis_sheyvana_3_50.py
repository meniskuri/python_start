import time


saxeli = input("sheiyvanet saxeli: ")


while(True):
    print("saxelia = ", saxeli)

    if len(saxeli) >= 3 and len(saxeli) <= 50:
        print("length of name must be great than 3 and less then 50, name is good")
        break
    else:
        print("length of name must be great than 3 and less then 50, enter new name")
        saxeli = input("sheiyvanet saxeli: ")
