import unittest
import string
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

    def test_encryption_rate(self):
        num_of_iterations = 5
        seed = time.time()
        alphabet = list(string.ascii_lowercase)
        key = OperKey.OperKey(num_of_iterations, seed, alphabet)
        num_of_logins = 1024 * 100

        # 5 Kb of logins
        users = ["admin" for x in range(num_of_logins)]

        start = time.time()
        for user in users:
            Oper.Oper.encrypt_string(key, user)
        end = time.time()

        if end - start > 0:
            print(str((len("admin") * num_of_logins)/(end - start))+'enc')
        print(end - start)

    def test_decryption_rate(self):
        num_of_iterations = 5
        seed = time.time()
        alphabet = list(string.ascii_lowercase)
        key = OperKey.OperKey(num_of_iterations, seed, alphabet)
        num_of_logins = 1024 * 100

        # 5 Kb of logins
        users = ["admin" for x in range(num_of_logins)]
        encrypted_users = []

        for user in users:
            Oper.Oper.encrypt_string(key, user)

        encrypted_volume = 0
        for user in users:
            encrypted_volume += len(str(user))

        start = time.time()
        for user in encrypted_users:
            Oper.Oper.decrypt_string(key, user)
        end = time.time()

        if end - start > 0:
            print(str((encrypted_volume / (end - start)))+'dec')
        print(end - start)
