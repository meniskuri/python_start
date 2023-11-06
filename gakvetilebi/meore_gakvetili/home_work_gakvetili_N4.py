print("savarjisho 1")

i = 4
while i <= 10:
    print(i)
    i = i + 4

print("savarjisho 1 - done")




print("savarjisho 2 - faqtorialis gamotvla (while loop it)")
number     = int(input("input any number: "))
faqtoriali = 1
i          = 1
while i <= number:
    faqtoriali = faqtoriali * i
    i = i + 1

print("Factorial of ", number, " is ", faqtoriali)
print("savarjisho 2 - done")




print("savarjisho 3 - for ciiklit (hello world)")
for i in 'hello world':   # ციკლი დაივლის თითო ასოზე მოცემულ ტექსტში
    print(i * 3, end='\n')  # ციკლის ცვლადში მოთავსებული მნიშვნელობა გავასამოდ და გამოვიტანოთ მიმდევრობით

for i in 'hello world':
    if i == 'l':
        continue
    else:
        print(i, end='')

for i in range(1, 10):         # ძირითადი ციკლი - სტრიქონები
    for j in range(1, 10):     # ჩაშენებული ციკლი - სვეტები
        print(i * j, end="\t") # end="\t" ტაბულაცია მნიშვნელობებს შორის
    print("\n")
print("savarjisho 3 - done")



print("savarjisho 4 - faqtorialis da misi jamis gamotvla (while loop it)")
number     = int(input("input any number: "))
faqtorial_jami = 0
faqtoriali = 1
i          = 1
while i <= number:
    faqtoriali = faqtoriali * i
    print("factorial = ", faqtoriali)
    i = i + 1
    faqtorial_jami = faqtorial_jami + faqtoriali
    print("factorial jami = ", faqtorial_jami)

print("Factorial of ", number, " is ", faqtoriali, "; factorialis jami ", faqtorial_jami)
print("savarjisho 2 - done")
