import OperKey


class Oper(object):
    @staticmethod
    def encrypt(key: OperKey.OperKey, plain):
        for i in range(key.num_of_iterations):
            exp = Oper.get_expansion(plain, key.radixes[2 * i])
            key.set_max_len(len(exp))
            for m in range(len(exp)):
                exp[m] += key.addintional_cfs[i][m + 1]
            plain = Oper.get_decimal_number(exp, key.radixes[2 * i + 1])

        return plain

    @staticmethod
    def decrypt(key: OperKey.OperKey, cipher):
        for i in range(key.num_of_iterations - 1, -1, -1):  # go reverse
            exp = Oper.get_expansion(cipher, key.radixes[2 * i + 1])
            for m in range(len(exp)):
                exp[m] -= key.addintional_cfs[i][m + 1]
            cipher = Oper.get_decimal_number(exp, key.radixes[2 * i])

        return cipher

    @staticmethod
    def get_expansion(source: int, radix: int) -> object:
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
