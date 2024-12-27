temperature = int(input("Enter temperature in Celsius: "))
if temperature > 40:
    print("Hot")
elif 20 <= temperature <= 39:
    print("Warm")
elif temperature < 20:
    print("Cold")
