print('''
#########################################################
Chess Board Coordinates
X coord (1-A 2-B 3-C 4-D 5-E 6-F 7-G 8-H)
Y coord (1 2 3 4 5 6 7 8)

Enter integers in range 1 to 8

X1 and Y1 are first square coordinates (entered by user)
X2 and Y2 are second square coordinates (entered by user)

Program will chek colours of squares and print the answer
#########################################################
''')

chekvector         = ["1", "2", "3", "4", "5", "6", "7", "8"] # list (vector) with correct coordinates
squareFirstcolour  = "" # first square colour
squareSecondcolour = "" # second square colour


while True:

    X1 = input("Enter X1 coordinate (if break type: exit): ") # X coord (1-A 2-B 3-C 4-D 5-E 6-F 7-G 8-H)
    print("id(X1) ",id(X1))
    print("type(X1) = ",type(X1))
    if X1 == "exit":
        print("amovagde while idan")
        break

    Y1 = input("Enter Y1 coordinate (if break type: exit): ") # Y coord (1 2 3 4 5 6 7 8)
    print("id(Y1) ",id(Y1))
    print("type(Y1) = ",type(Y1))
    if Y1 == "exit":
        print("amovagde while idan")
        break

    X2 = input("Enter X2 coordinate (if break type: exit): ")
    print("id(X2) ",id(X2))
    print("type(X2) = ",type(X2))
    if X2 == "exit":
        print("amovagde while idan")
        break

    Y2 = input("Enter Y2 coordinate (if break type: exit): ")
    print("id(Y2) ",id(Y2))
    print("type(Y2) = ",type(Y2))
    if X1 == "exit" or X2 == "exit" or Y1 == "exit" or Y2 == "exit":
        print("amovagde while idan")
        break


    if X1 in chekvector:
        print("X1 in chekvetor")

        if (int(X1) > 0 and int(X1) < 9) and (int(X2) > 0 and int(X2) < 9) and (int(Y1) > 0 and int(Y1) < 9) and (int(Y2) > 0 and int(Y2) < 9):
            print("kargi reinjia")
            # string symbols to ints
            X1 = int(X1)
            Y1 = int(Y1)
            X2 = int(X2)
            Y2 = int(Y2)

                # Chek first square colour
            if ((X1 % 2 == 0) and (Y1 % 2 == 0)) or ((X1 % 2 != 0) and (Y1 % 2 != 0)):
                squareFirstcolour = "Black"
                print(f"First square is {squareFirstcolour}")
            else:
                squareFirstcolour = "White"
                print(f"First square is {squareFirstcolour}")


            # Chek second square colour
            if ((X2 % 2 == 0) and (Y2 % 2 == 0)) or ((X2 % 2 != 0) and (Y2 % 2 != 0)):
                squareSecondcolour = "Black"
                print(f"Second square is {squareSecondcolour}")
            else:
                squareSecondcolour = "White"
                print(f"Second square is {squareSecondcolour}")

            # print message
            if squareFirstcolour == squareSecondcolour:
                print(f"YES, they have same colour, colour is {squareSecondcolour}")
            else:
                print(f"NO, they d't have same colour, first square colour is {squareFirstcolour} and second square colour is {squareSecondcolour}")


        else:
            print("ragac geshleba - sheiyvane ricxvebi swor reinjshi")
            continue
    else:
        print("ragac geshleba - sheyvanili ricxvi ar aris reinjshi")
        print("reinji 1, 2, 3, 4, 5, 6, 7, 8")
