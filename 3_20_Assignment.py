while True:
    event_year = int(input("Enter the event year: "))
    if event_year >= 1970:
        print("Valid Year")
        break
    else:
        print("\n Enter the valid year \n")

while True:
    event_month = int(input("Enter the event month: "))
    if event_month >= 1 and event_month <= 12:
        print("Valid Month")
        break
    else:
        print("\n Enter the valid month \n")

thirtydays = [4, 6, 9, 11]
thirtyonedays = [1, 3, 5, 7, 8, 10, 12]
while True:
    event_day = int(input("Enter the event day: "))

    if event_year % 4 == 0 and event_year % 400 == 0:
        if event_month in thirtydays:
            if event_day >= 1 and event_day <= 30:
                print("It is the month of April, June, Sep or Dec")
                break
            else:
                print("\n Please enter correct day")

        elif event_month in thirtyonedays:
            if event_day >= 1 and event_day <= 31:
                print("It is the month of Jan, Mar, May, July, Aug,Oct or Dec ")
                break
            else:
                print("\n Please enter correct day")
        else:
            if event_day >= 1 and event_day <= 29:
                print("It is the month of Feb and is a leap year")
                break
            else:
                print("\n Please enter correct day in the month of February")

    else:
        if event_month in thirtydays:
            if event_day >= 1 and event_day <= 30:
                print("It is the month of April, June, Sep or Dec")
                break
            else:
                print("\n Please enter correct day")

        elif event_month in thirtyonedays:
            if event_day >= 1 and event_day <= 31:
                print("It is the month of Jan, Mar, May, July, Aug,Oct or Dec ")
                break
            else:
                print("\n Please enter correct day")
        else:
            if event_day >= 1 and event_day <= 28:
                print("It is the month of Feb and is not a leap year")
                break
            else:
                print("\n Please enter correct day in the month of February")
