alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('Please enter your key: '))
newMessage = ''
message = input('Please enter your message: ')
for character in message:
	if character in alphabet:
		position = alphabet.find(character)
		newPosition = (position + key) % 26
		newCharacter = alphabet[newPosition]
		newMessage += newCharacter
	else:
		newMessage += character
print(newMessage)
