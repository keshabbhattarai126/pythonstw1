weather = input("Enter the weather (sunny/rainy): ")

if weather == "sunny":
    print("You can go for hiking or have a picnic!")
elif weather == "rainy":
    raincoat_or_umbrella = input("Do you have a raincoat or umbrella? (yes/no): ")
    if raincoat_or_umbrella == "yes":
        print("You can go to a nearby mall or museum!")
    else:
        print("It's better to stay home and watch movies.")
else:
    print("Invalid weather input. Please enter 'sunny' or 'rainy'.")
