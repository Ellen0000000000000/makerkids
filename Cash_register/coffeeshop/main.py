espresso_price = 2.50
americano_price = 3.00
latte_price = 2.50
cappuccino_price = 3.00
macchiato_price = 2.50
mocha_price = 3.50
flatwhite_price = 2.50

medium_price = 0.00
large_price = 1.00
XL_price = 1.50

eat-in_price = 0.00
Takeaway_price = 1.00

price = 0
espresso = input("Do you want espresso? ")
if espresso.upper() == "YES":
    price = price + espresso_price

americano = input("Do you want americano? ")
if americano.upper() == "YES":
    price = price + americano_price

latte = input("Do you want latte?")
if latte.upper() == "YES":
    price = price + latte_price

cappuccino = input("Do you want a cappuccino?")
if cappuccino.upper() == "YES":
    price = price + cappuccino_price
    
macchiato = input("Do you want a macchiato?")
if macchiato.upper() == "YES":
    price = price + macchiato_price

mocha = input("Do you want a mocha?")
if mocha.upper() == "YES":
    price = price + mocha_price

flatwhite = input("Do you want a flatwhite?")
if flatwhite.upper() == "YES":
    price = price + flatwhite_price

size = input("What size? ")
if size.upper() == "MEDIUM":
    price = price + medium_price
if size.upper() == "LARGE":
    price = price + large_price
if size.upper() == "XL":
    price = price + XL_price

eat_in/takeaway = input("Do you want to eat here?")
if size.upper() == "YES":
    price = price + eat-in_price
if size.upper() == "NO":
    price = price + Takeaway_price

print("your total is $" + str(price))

