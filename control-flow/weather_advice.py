# -------------------------------------------------
# Create a script that works with uses COntrol flow 
#---------------------------------------------------

def weather_clothing(): 
    weather = input("What's the weather like today? (sunny/rainy/cold):").lower()

    if(weather == "sunny"): 
        return print("Wear a t-shirt and sunglasses.")
    if(weather == "rainy"):
        return print("Don't forget your umbrella and a raincoat.")
    if(weather =="cols"): 
        return print("Make sure to wear a warm coat and a scarf.")
    else:
        return print("Sorry, I don't have recommendations for this weather.")

weather_clothing()