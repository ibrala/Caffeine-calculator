run = "yes"

while run.lower() == "yes":

    caffeine_amount = float(input("enter the amount of caffeine in mg in the drink: "))
    drink_size = float(input("enter the size of the drink in dl: "))

    percent = (100 - 13) / 100

    if 30 <= caffeine_amount <= 130:
        if 0.3 <= drink_size <= 5:
            content = caffeine_amount * drink_size

            one_unit = content
            print("caffeine content in the body after one unit is", format(one_unit, '.1f'), "mg")

            one_hour = content * percent
            print("caffeine content in the body after 1 hour is", format(one_hour, '.1f'), "mg")

            five_hours = content * (percent ** 5)
            print("caffeine content in the body after 5 hours is", format(five_hours, '.1f'), "mg")

            twelve_hours = 0
            for t in range(1, 14):
                twelve_hours = twelve_hours * percent + content
            print("caffeine content in the body after", t, "hours with one unit per hour is", format(twelve_hours, '.1f'), "mg")
        else:
            print("invalid value for drink size, please enter a value between 0.3–5 dl")
    else:
        print("invalid value for caffeine amount, please enter a value between 30–130 mg")

    valid_answer = False
    while not valid_answer:
        run_input = input("do you want to run this program again? (yes/no/nei) ").lower()
        if run_input in ["yes", "no"]:
            run = run_input
            valid_answer = True
        else:
            print("please enter a valid answer: yes, no, or nei")

print("program finished")
