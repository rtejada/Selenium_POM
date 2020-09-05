import uuid
import random
import string
import requests

num = random.randint(97, 122)
print(chr(num))


word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()

print('OJO')

guid_num = int(uuid.uuid4())
guid_let = str(uuid.uuid4())
print(guid_let)
keywords = guid_let.split("-")
print(keywords[0])


guid_num_let = uuid.uuid4().hex
print(uuid.uuid1())
print(guid_num)
print(guid_let)
print('lestras:',guid_num_let)
print("MAC address integer format", str(uuid.getnode()))
print("MAC address Hex format", hex(uuid.getnode()))

for i in range(2):
    uuidFour = uuid.uuid4()
    print("uuid of version four", uuidFour)


random.choice(string.ascii_letters)


def random_char(y):

    return ''.join(random.choice(string.ascii_letters) for x in range(y))


print(random_char(7))


import random as r


def generate_uuid():
        random_string = ''
        random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        uuid_format = [8, 4, 4, 4, 12]
        for n in uuid_format:
            for i in range(0,n):
                random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
            if n != 12:
                random_string += '-'
        return random_string

print(generate_uuid())


from random_word import RandomWords

r = RandomWords()

# Return a single random word
print('Roxana', r.get_random_word())
# Return list of Random words
print(r.get_random_words())
# Return Word of the day
print('Prueba:', r.word_of_the_day())

'''

list1=[a,b,c,d,e,f,g,h]
b=random.randint(0,7)

print(list1[b])
'''