cup_price = 0.50
cone_price = 0.80
scoop_price = 1.20
flake_price = 0.40
chocolate_price = 0.30
strawberry_price = 0.60

price = 0
container = input("Would you like a cup or cone? ")
if container.upper() == "CUP":
    price = price + cup_price
else:
    price = price + cone_price

scoops = int(input("How many scoops? "))
price = price + (scoops * scoop_price)


flakes = input("do you want flakes? ")
if flakes.upper() == "YES":
    price = price + flake_price

chocolate = input("Do you want chocolate sprinkles? ")
if chocolate.upper() == "YES":
    price = price + chocolate_price

strawberry = input("Do you want strawberry coulis? ")
if strawberry.upper() == "YES":
    price = price + strawberry_price


print("your total is $" + str(price))