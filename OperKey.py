import random
import string
from itertools import permutations


class OperKey(object):
    """"parameters of encryption"""
    num_of_iterations = 10
    max_radix = 10000000
    base_len = 64
    step = 30
    """key data"""
    seed = 1495981489.569693
    radixes = []
    addintional_cfs = [[0 for x in range(1)] for y in range(1)]
    alphabet = list(string.ascii_lowercase)

    def __init__(self, num_of_iterations=10, seed=1495981489.569693, alphabet=list(string.ascii_lowercase)):
        self.seed = seed
        random.seed(self.seed)
        self.num_of_iterations = num_of_iterations
        self.alphabet = alphabet
        self.generate_radixes()
        self.generate_coefficients()
        self.generate_alphabet_permutation()

    def __str__(self):
        key = "[ [seed: " + self.seed.__str__() + " ]\n" + \
              "[ num of iter: " + self.num_of_iterations.__str__() + " ]\n" + \
              "[ radixes: " + self.radixes.__str__() + " ]\n" + \
              "[ additional cfs: " + self.addintional_cfs.__str__() + " ] ]"

        return key

    # устанавливает длину векторов дополнительных коэффициентов максимальной
    def set_max_len(self, length):
        if len(self.addintional_cfs[0]) == length + 1:
            return
        for it in range(self.num_of_iterations):
            for i in range(length):
                self.addintional_cfs[it].append(random.randint(0, self.radixes[it * 2 + 1] - self.radixes[it * 2]))

    def generate_radixes(self):
        self.radixes.append(random.randint(2, self.step))

        for i in range(1, self.num_of_iterations * 2):  # each iteration demands two radixes
            self.radixes.append(random.randrange(self.radixes[i - 1] + 2, self.radixes[i - 1] + self.step, 2))

    def generate_coefficients(self):
        for i in range(self.num_of_iterations - 1):
            self.addintional_cfs.append([0 for x in range(1)])

    def generate_alphabet_permutation(self):
        # number of all permutations
        numberOfPerms = 3 #math.factorial(len(self.alphabet))
        # random num less then numbers of all permutations
        selected_permutation = numberOfPerms #randrange(numberOfPerms) % 1000
        perms = permutations(self.alphabet)

        # get random permutation
        for i in range(selected_permutation):
            next(perms)

        # fix chosen permutation
        self.alphabet = next(perms)

        # let's test with this one
        self.alphabet = ['g', 'h', 'b', 'c', 'j', 'u', 'i', 'k', 'd', 'e', 'f', 'l', 't', 'a', 'm', 'p', 'q', 'r', 's', 'n', 'o',
                'v', 'w', 'x', 'y', 'z']
