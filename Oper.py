import OperKey


class Oper(object):
    @staticmethod
    def encrypt_string(key: OperKey.OperKey, plain: str):
        return Oper.encrypt_number(key, Oper.encode_string_with_permuted_alphabet(key, plain))

    @staticmethod
    def encrypt_number(key: OperKey.OperKey, plain):
        source = plain
        for i in range(key.num_of_iterations):
            expansion = Oper.get_expansion(int(source), key.radixes[2 * i])
            key.set_max_len(len(expansion))
            for m in range(len(expansion)):
                expansion[m] += key.addintional_cfs[i][m + 1]
            source = Oper.get_decimal_number(expansion, key.radixes[2 * i + 1])

        return source

    @staticmethod
    def decrypt_string(key: OperKey.OperKey, cipher):
        semi_result = Oper.decrypt_number(key, cipher)
        return Oper.decode_string_with_permuted_alphabet(key, str(semi_result))


    @staticmethod
    def decrypt_number(key: OperKey.OperKey, cipher):
        for i in range(key.num_of_iterations - 1, -1, -1):  # go reverse
            expansion = Oper.get_expansion(cipher, key.radixes[2 * i + 1])
            for m in range(len(expansion)):
                expansion[m] -= key.addintional_cfs[i][m + 1]
            cipher = Oper.get_decimal_number(expansion, key.radixes[2 * i])

        return cipher

    @staticmethod
    def get_expansion(source: int, radix: int):
        cfs = []

        while source > 0:
            cfs.append(source % radix)
            source = source // radix

        return cfs

    @staticmethod
    def get_decimal_number(expansion, base):
        result = 0
        for i in range(len(expansion)):
            result += expansion[i] * base ** i
        return result

    # Returns a string which is transformed input string.
    # Letters replaced with numbers of their positions in permuted alphabet
    @staticmethod
    def encode_string_with_permuted_alphabet(key: OperKey, source: str):
        # start with '1' in order to avoid numbers starting with '0'
        middle_num_str = '1'

        # get string representation in numbers which are positions of letters in alphabet
        for w in source:
            letter_position = key.alphabet.index(w)
            # we replace a letter with a number which has two ciphers
            if letter_position < 10:
                middle_num_str += '0' + str(letter_position)
            else:
                middle_num_str += str(letter_position)

        return middle_num_str

    @staticmethod
    def decode_string_with_permuted_alphabet(key: OperKey, source: str):
        # first sign is not meaningful
        encoded = source[1:]
        decoded = ""

        # each letter is presented with 2 signs
        for i in range(int(len(encoded) / 2)):
            start_position = 2 * i
            end_position = 2 * (i + 1)
            decoded += key.alphabet[int(encoded[start_position: end_position])]

        return decoded
