for x in range(2):
    print("xxxxxxxxxx")
    for y in range(1):
        print("xx")
print('''xx

''')



numbers = [5,2,7,22,2]
i = 0
for x in numbers:
    print("x" * int(numbers[i]))
    i = i + 1

for x in numbers:
    gamosavali = ""
    for y in range(x):
        gamosavali = gamosavali + "y"
    print(gamosavali)


saxelebi = ["გიო","vaso","levaniko","luka","teo","azo"]
გიოია = saxelebi[:3]
print(გიოია)

maqsimumi = numbers[0]
i = 0
for x in numbers:
    if numbers[i] > maqsimumi:
        maqsimumi = numbers[i]
        print(i)
    i = i + 1

print(maqsimumi)
