weather_conditions = ["sunny", "rainy", "snowy"]
weather = "Snowy"
weather = weather.lower()

if weather in weather_conditions:
    if weather == "sunny":
        activity = "Go for a walk"
    elif weather == "rainy":
        activity = "Read a book"
    else:
        activity = "Build a snowman"
    
    print(f"The weather is {weather} today. You should '{activity}'")
else:
    print("Please enter weather in this list: sunny, rainy, snowy")