# caffeine calculator task
# this program will calculate the caffeine content in the body based on user input

# sets variable that controls whether the program should run again
run = "yes"

# as long as the user answers yes
while run == "yes":
    # input from the user
    caffeine_amount = float(input("enter the amount of caffeine in mg in the drink: "))
    drink_size = float(input("enter the size of the drink in dl: "))

    # caffeine is broken down in the body by 13% per hour
    percent = (100 - 13) / 100

    # check that the given values are valid
    if caffeine_amount >= 30 and caffeine_amount <= 130:
        if drink_size >= 0.3 and drink_size <= 5:
            content = caffeine_amount * drink_size

            # calculate caffeine content
            one_unit = content
            print("caffeine content in the body after one unit is", format(one_unit, '.1f'), "mg")

            one_hour = content * percent
            print("caffeine content in the body after 1 hour is", format(one_hour, '.1f'), "mg")

            five_hours = content * (percent ** 5)
            print("caffeine content in the body after 5 hours is", format(five_hours, '.1f'), "mg")

            twelve_hours = 0
            for t in range(1, 13, 1):
                twelve_hours = twelve_hours * percent + content
            print("caffeine content in the body after", t, "hours with one unit per hour is", format(twelve_hours, '.1f'), "mg")

        else:
            print("invalid value for drink size, please enter a value between 0.3-5 dl")
    else:
        print("invalid value for caffeine amount, please enter a value between 30-130 mg")

    # ask if the user wants to run the program again
    run = input("do you want to run the program again? yes/no ")
print("program finished")
