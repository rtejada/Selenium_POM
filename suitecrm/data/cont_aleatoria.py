from secrets import choice
from string import ascii_letters, ascii_uppercase, digits

characters = ascii_letters + ascii_uppercase + digits
length = 5
random_chain = ''.join(choice(characters) for char in range(length))

print(random_chain)