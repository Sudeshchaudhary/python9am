while True:
    event_year = int(input("Enter the year:"))
    if event_year < 1980:
        print("Enter the valid year")
    else:
        print("Valid year")
        break
while True:
    event_month = int(input("Enter the month:"))
    if event_month >= 1 and event_month <= 12:
        print("Valid month")
        break
    else:
        print("Enter the valid month")

thirtydays = [4, 6, 9, 11]
thirtyonedays = [1, 3, 5, 7, 8, 10, 12]
while True:
    event_day = int(input("Enter the day:"))

    if event_month in thirtydays:
        if event_day >= 1 and event_day <= 30:
            print("This is leap year and month of 30 days")
            break
        else:
            print("Enter the valid day")
    elif event_month in thirtyonedays:
        if event_day >= 1 and event_day <= 31:
            print("This is leap year and month of 31 days")
            break
        else:
            print("Enter the valid day")
    elif event_month==2:
        if event_day >= 1 and event_day <= 28:
            print("It is month of February and is not a leap year")
            break
        else:
            print("Enter the valid day of February")

    if event_year % 4 == 0 and event_year % 400 == 0:

        if event_day >= 1 and event_day <= 29:
            print("It is month of February and is a leap year")
            break
        else:
            print("Enter the valid day of February leap year")
