import os

import math

from Oper import Oper
from OperKey import OperKey


class FileHasher(object):
    key = OperKey()

    # @staticmethod
    def get_file_hash(self, filename: str):
        leaves = FileHasher.prepare_leaves(filename)
        file_hash = FileHasher.get_hash(self, leaves)
        return file_hash

    @staticmethod
    def prepare_leaves(filename: str):
        file_size = os.path.getsize(filename)
        batch_size = 5
        steps = int(math.ceil(file_size / batch_size))
        leaves = []

        for pos in range(steps):
            with open(filename, "rb") as binary_file:
                binary_file.seek(pos * batch_size)
                data = binary_file.read(batch_size)
                leaves.append(int.from_bytes(data, 'little'))

        return leaves

    # @staticmethod
    def get_hash(self, leaves):
        tree_depth = int(math.log(len(leaves), 2))
        current_level_leaves = leaves

        for x in range(tree_depth):
            current_level_leaves = FileHasher.process_leaves(self, current_level_leaves)

        return current_level_leaves[0]

    # @staticmethod
    def process_leaves(self, leaves):
        new_leaves = []
        for x in range(len(leaves) // 2):
            for_current_level_root = str(leaves[2 * x]) + str(leaves[2 * x + 1])
            new_leaves.append(Oper.encrypt_number(self.key, for_current_level_root))

        return new_leaves
