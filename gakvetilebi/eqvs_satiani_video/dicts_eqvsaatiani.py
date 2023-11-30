gadamyvani = {
  "1":"erti",
  "2":"ori",
  "3":"sami",
  "4":"otxi",
  }


while True:
    phone = input("Phone (exit the program -> exit <-): ")
    if phone == "" or phone == "exit":
        break
    print(gadamyvani.get(phone,"rame"))
