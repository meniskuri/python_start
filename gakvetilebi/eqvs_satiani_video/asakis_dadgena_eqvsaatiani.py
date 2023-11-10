from datetime import datetime

def get_current_year():
    # Get the current date and time
    current_datetime = datetime.now()

    # Extract the year from the current date
    current_year = current_datetime.year
    current_time = current_datetime
    print("time: ",current_time)

    return current_year

# Call the function to get the current year

weli = get_current_year()

# Print the result
print("Current Year:", weli)

saxeli           = input("input your name: ")
dabadebis_tarigi = int(input("dabadebis tarigi: "))
asaki            = weli - dabadebis_tarigi
print("saxelia: ",saxeli,"; dabadebis tarigia: ",dabadebis_tarigi,"; asaki: ",asaki)
