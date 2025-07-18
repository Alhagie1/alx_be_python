
# A Weather Recommendation Program
weather_conditon = input("What is the weather like today? (sunny/rainy/cold):")

if weather_conditon == "sunny":
    print("Wear a t-shirt and sun glasses")
elif weather_conditon == "rainy":
    print("Don't forget your umbrella and raincoat")
elif weather_conditon == "cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry I don't have recommendation for this weather")
