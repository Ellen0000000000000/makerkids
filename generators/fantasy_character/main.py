import random

first_names = ["Ava", "jim", "bob", "jane", "ted", "mary"]
last_names = ["jane", "tim", "slim", "john", "fred", "beth"]
species = ["human", "elf", "unicorn", "flying pig", "dragon", "fairy"]
powers = ["teleportation", "invisibility", "flying", "healing", "lightning", "fire"]

first_name = random.choice(first_names)
last_name = random.choice(last_names)
email = first_name + "." + last_name + "@gmail.com"
specie = random.choice(species)
power = random.choice(powers)

print("Here is your randomly generated character:")
print("Name: " + first_name + " " + last_name)
print("Species: " + specie)
print("Magical power: " + power)

