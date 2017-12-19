import string
import unittest
import time
import Oper
import OperKey


class OperTest(unittest.TestCase):

    def test_encryption(self):
        num_of_iterations = 5
        seed = time.time()
        alphabet = list(string.ascii_lowercase)
        key = OperKey.OperKey(num_of_iterations, seed, alphabet)

        users = ['admin', 'diana', 'bella']
        encrypted_users = []
        decrypted_users = []

        for user in users:
            encrypted_users.append(Oper.Oper.encrypt_string(key, user))

        for user in encrypted_users:
            decrypted_users.append(Oper.Oper.decrypt_string(key, user))

        self.assertEqual(users, decrypted_users)
