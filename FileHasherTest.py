import unittest

from FileHasher import FileHasher


class FileHasherTest(unittest.TestCase):

    def test_get_file_hash(self):
        fh = FileHasher()
        fh.get_file_hash("C:\\Users\\diana\\Documents\\Аспирантура\\tst.txt")
        self.assertEqual(1, 1)
