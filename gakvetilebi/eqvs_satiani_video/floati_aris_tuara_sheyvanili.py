# Custom boolean function
def is_float(string):
    try:
# Return true if float
        float(string)
        return True
    except ValueError:
# Return False if Error
        return False

sheyvana = input("sheiyvanet ricxvi: ")

print(is_float(sheyvana))
