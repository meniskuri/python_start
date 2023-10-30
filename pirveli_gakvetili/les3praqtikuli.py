# pirobebis operatorebi

age = int(input("sheitanet tqveni asaki: "))

if True:
    print("ok )))")
    if age > 30:
        print("srulwlovani xart")

# amocana N1
age = int(input("dawere sheni asaki: "))

if age < 18:
    print("araswrulwlovani xart")
elif age >= 30 and age < 70:
    print("tqven srulwlovani xart")
elif age >= 70:
    print("aba exla ukve mtavari amocanebi shesrulebuli unda gqondes. tu bonusi ar ginda")
else:
    print("ravi aba ")



if age > 18 and age < 20:
    print("pirveli")
elif age > 25:
    print("meore")
elif age > 30:
    prit("mesame")


# amocana N2
x = int(input("sheiyvane x: "))
y = int(input("sheiyvane y: "))


if x > y:
    print(f"umciresia y: {y}")
elif x < y:
    print(f"umciresia x: {x}")
elif x == y:
    print(f" x = y")



# amocana N3

k = int(input("sheiyvanet K: "))

if k < 0:
    print("negativ")
elif k > 0:
    print("positive")


# amocana N4

qula = int(input("sheiyvanet qula: "))

if qula < 0 or qula > 100:
    print("araswori monacemi")
elif qula >= 0 and qula <= 41:
    print("tqveni shefasebaa: F")
elif qula >= 42 and qula <= 51:
    print("tqveni shefasebaa: Fx")
elif qula >= 52 and qula <= 62:
    print("tqveni shefasebaa: E")
elif qula >= 63 and qula <= 72:
    print("tqveni shefasebaa: D")
elif qula >= 72 and qula <= 100:
    print("tqveni shefasebaa: A")

# amocana N5. ვალუტის კონვერტატორი


USD = 3.4
EUR = 4

print("1. GEL")
print("2. USD")
print("3. EUR")

curency = input("airchiet N: ")
amount  = int(input("amount: "))

print("1. GEL")
print("2. USD")
print("3. EUR")

convert = input("choose currency to convert: ")

if curency == "GEL":
    if convert == "USD":
        print(amount/USD)
    elif convert == "EUR":
        print(amount/EUR)


elif curency == "USD":
    if convert == "GEL":
        print(amount*USD)
    elif convert == "EUR":
        print(amount/1.2039)


elif curency == "EUR":
    if convert == "GEL":
        print(amount*EUR)
    elif convert == "EUR":
        print(amount*1.2039)



# amocana N6. კონვერტერი მილები კილომეტრებში და ეგრე
print("1. m")
print("2. km")
print("3. mile")

value = input("airchiet manzilis erteuli: ")
distance = int(input("sheitanet manzili: "))

convert = input("airchiet sad gadagvyavs: ")


if value == "m" or value == "1":
    if convert == "km" or convert == "2":
        print(distance / 1000)


elif value == "km" or value == "2":
    if convert == "m" or convert == "1":
        print(distance * 1000)

    elif convert == "mile" or convert == "3":
        print(distance / 1.621)
elif value == "mile" or value == "3":

    if convert == "km" or convert == "2":
        print(distance * 1.621)


###########################################################################
# დავწერო ჩემი კონვერტერი ##################################################





###########################################################################
# დავწერო ჭადრაკის ამოცანა #################################################
