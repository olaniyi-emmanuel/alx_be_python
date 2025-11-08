# Calculator of some sort of age calculation  
import datetime 

def age_calulator(): 
    #_year = 2
    user_age = int(input("How Old are you: "))
    #year_to_be_calculated = input("What year do you want to calculate your age to: ")
    #year_of_birth = datetime.date.today().year - user_age - _year
    #future_age = int(year_to_be_calculated) - year_of_birth
    real_age_in_future = user_age + 27 
    return print(f"In 2050, you will be {real_age_in_future} years old.")
age_calulator()

