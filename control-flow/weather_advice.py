# -------------------------------------------------
# Create a script that works with uses COntrol flow 
#---------------------------------------------------

def weather_clothing(): 
    message = input("What's the weather like today? (sunny/rainy/cold):").lower()

    if(message == "sunny"): 
        return print("Wear a t-shirt and sunglasses.")
    elif(message == "rainy"):
        return print("Don't forget your umbrella and a raincoat.")
    elif(message =="cols"): 
        return print("Make sure to wear a warm coat and a scarf.")
    else:
        return print("Sorry, I don't have recommendations for this weather.")

weather_clothing()