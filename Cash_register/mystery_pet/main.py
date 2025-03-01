import random

pet_names = ["1", "2", "3", "4", "5"]
pet_species = ["Cat", "Dog", "Dragon", "Hamster", "Unicorn"]
pet_traits = ["Boring", "flies","dumb", "loud", "annoying"]


user_collection = []


def generate_mystery_pet():
    name = random.choice(pet_names)
    species = random.choice(pet_species)
    traits = random.choice(pet_traits)

    pet = {
        "Name": name,
        "Species": species,
        "Trait": traits
    }
    return pet


def display_pet(pet):
    print("Mystery Pet Details: ")
    print("Name: " + pet["Name"])
    print("Species: " + pet["Species"])
    print("Special Trait: " + pet["Trait"])


def mystery_pet_shop():
    print("Welcome to the mystery pet shop")

    while True:
        action = input("Would you like to buy or exit?")
        if action == "exit":
            print("Thanks for visiting")
            break
        elif action == "buy":
            pet = generate_mystery_pet()
            display_pet(pet)

            decision = input("would you like to buy? yes or no")

            if decision == "yes":
                user_collection.append(pet)
                print(pet["Name"] + " was added to your cart")
            else:
                print("no worries let's try another pet")
        else:
            print("plz type exit or buy")


my_pet = generate_mystery_pet()
display_pet(my_pet)
#print(my_pet)

