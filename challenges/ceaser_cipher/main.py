alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_message = ''

key = int(input("Please enter a key: "))

message = input("Please enter a message: ")

for character in message:

    position = alphabet.find(character)

    new_position = (position + key) % 26

    new_character = alphabet[new_position]

    new_message += new_character

print(new_message)

