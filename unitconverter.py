
# While loop to start the conversion app
while True:
    print("\nSelect conversion!\n")
    print("[1] Distance")
    print("[2] Temperature")
    print("[3] Time")
    print("[4] Exit\n")

    # Choice inputs
    choice = input("[1] [2] [3] [4] : ")

    # Exit choice
    if choice == "4":
        print("\nExiting...")
        break


    elif choice == "1":
        while True:
            print("\nDistance Conversion")
            print("[1] Miles to Kilometers")
            print("[2] Kilometers to Miles")
            print("[3] Back to Menu\n")
            dist_choice = input("[1] [2] [3] : ")


            if dist_choice == "1":
                print("\n\033[1mYou chose Miles to Kilometers\033[m")
                mtokm = float(input("How many miles? : "))
                print(f"\n{mtokm} miles is equal to {mtokm * 1.621371:.2f} kilometers!")


            #    ask for input and convert

            elif dist_choice == "2":
                print("\n\033[1mYou chose Kilometers to Miles\033[m")
                kmtom = float(input("How many kilometers? : "))
                print(f"\n{kmtom} kilometers is equal to {kmtom / 1.621371:.2f} miles!")

            #    ask for input and convert

            elif dist_choice == "3":
                # loops back to menu
                break

            else:
                print("Invalid option... Try again")

    elif choice == "2":
        while True:
            print("\nTemperature Conversion")
            print("[1] C to F")
            print("[2] F to C")
            print("[3] Back to Menu\n")
            temp_choice = input("[1] [2] [3] : ")

            if temp_choice == "1":
                print("\n\033[1mYou chose C to F\033[m")
                c2f = float(input("What is the temperature? : "))
                fahrenheit =  (c2f * 9/5) + 32
                print(f"{c2f} degrees in Celsius is equivalent to {fahrenheit:.2f} degrees Fahrenheit!")

            elif temp_choice == "2":
                print("\n\033[1mYou chose F to C\033[m")
                f2c = float(input("What is the temperature? : "))
                celsius = (f2c - 32) * 5/9
                print(f"{f2c} degrees in Fahrenheit is equivalent to {celsius:.2f} degrees Celsius!")

            elif temp_choice == "3":
                break

            else:
                print("Invalid option... Try again")


    elif choice == "3":
        while True:
            print("\nTime Conversion")
            print("[1] Hours to Minutes")
            print("[2] Minutes to Hours")
            print("[3] Back to Menu\n")
            time_choice = input("[1] [2] [3] : ")

            if time_choice == "1":
                print("\n\033[1mYou chose Hours to Minutes\033[m")
                h2m = float(input("How many hours? : "))
                minutes = h2m * 60
                print(f"{h2m} hours is {minutes:.2f} minutes")

            elif time_choice == "2":
                print("\n\033[1mYou chose Minutes to Hours\033[m")
                m2h = float(input("How many minutes? : "))
                hours = m2h / 60
                print(f"{m2h} minutes is {hours:.2f} hours")

            elif time_choice == "3":
                break










