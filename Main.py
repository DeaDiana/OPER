import string
import time
from itertools import permutations
import math
from random import randrange
import Oper
import OperKey
################################# part of key ###################
# alphabet
alphabet = list(string.ascii_lowercase)
# number of all permutations
numberOfPerms = math.factorial(len(alphabet))
# random num less then numbers of all permutations
seed = 3#randrange(numberOfPerms) % 1000
# stream of all possible permutations of alphabet
perms = permutations(alphabet)
# get random permutation
for i in range(seed):
    next(perms)
# fix chosen permutation
perm = next(perms)
# let's test with this one
perm = ['g', 'h', 'b', 'c', 'j', 'u','i', 'k', 'd', 'e', 'f', 'l', 't', 'a', 'm', 'p', 'q', 'r', 's', 'n', 'o',  'v', 'w', 'x', 'y', 'z']
################################# part of key ###################

### test data #####
users = ['admin', 'diana', 'bella']

# Returns a string which is transformed input string.
# Letters replaced with numbers of thir positions in permuted alphabet
def map_username_with_permuted_alphabet(username):
    # start with '1' in order to avoid numbers starting with '0'
    source_num_str = '1'
    middle_num_str = '1'

    # get string representation in numbers which are positions of letters in alphabet
    for w in username:
        letter_position = alphabet.index(w)
        # we replace a letter with a number which has two ciphers
        if letter_position < 10:
            source_num_str += '0' + str(letter_position)
        else:
            source_num_str += str(letter_position)

    for w in username:
        letter_position = perm.index(w)
        if letter_position < 10:
            middle_num_str += '0' + str(letter_position)
        else:
            middle_num_str += str(letter_position)

    return middle_num_str

key = OperKey.OperKey(5, time.time())
encrypted_users = []

for user in users:
    transformed_user = map_username_with_permuted_alphabet(user)
    encrypted_users.append(Oper.Oper.encrypt(key, int(transformed_user)))

for i in range(len(users)):
    print(users[i], encrypted_users[i])

print(sorted(users))
print(sorted(encrypted_users))