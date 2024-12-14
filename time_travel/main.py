import json
import random

with open("ages.json", "r") as file:
    ages = json.load(file)

print("Welcome to the Time Machine!")
print("Travel through time and explore the wonders of history!")
print("Type the name of a time period or type exit to leave")
print("Avalible time periods: ")

for time_period in ages.keys():
    print(f" - {time_period}")

while True:
    user_choice = input("Where would you like to go?")

    if user_choice == "exit":
        print("Exiting the time machine")
        break
    elif user_choice in ages:
        print(f"you have travelled to the {user_choice}!")

        #selected age is the age user choice
        selected_age = ages[user_choice]
        #pick random invention from the age user choice
        invention = random.choice(selected_age["Inventions"])
        major_event = random.choice(selected_age["Major Events"])
        daily_life = random.choice(selected_age["Daily Life"])

        print(f"- a notable invention: {invention}")
        print(f"- a major historical event: {major_event}")
        print(f"- what daily life was like:{daily_life}")
        print("-------------------------------------------")
    
    else:
        print("Invalid time period. please choose from the avalible options")





#print(ages["Bronze Age"])
#print(ages["Bronze Age"]["Major Events"])
#print(ages["Islamic Golden Age"]["Inventions"])
#print(ages["Classical Era"]["Inventions"][0])
#print(ages["Future"]["Daily Life"][2])