
# A Weather Recommendation Program

# Asking for user's weather input
weather = input("What's the weather like today? (sunny/rainy/cold):").strip().lower()
# Giving recommendation based on provided weather conditions
if weather == "sunny":
    print("Wear a t-shirt and sun glasses")
elif weather == "rainy":
    print("Don't forget your umbrella and raincoat")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry I don't have recommendation for this weather")
