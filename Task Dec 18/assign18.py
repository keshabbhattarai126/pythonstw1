city_monument = {'Delhi':'Red Fort', 'Agra':'Taj Mahal','Jaipur':'Jal Mahal'}
city = input("Enter the name of city (Delhi/Agra/Jaipur) to display the monument of that city")
if (city in city_monument):
    result = city_monument[city]
    print(result)
else:
    print("The city is not in database")