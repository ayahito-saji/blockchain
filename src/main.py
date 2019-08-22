# coding: UTF-8

import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        create new block and push chain
        :param proof: <int> the proof which is get from proof of work algorithm
        :param previous_hash: <str> the hash of previous block
        :return: <dict> a block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        create new transaction and push list
        :param sender: <str> the address of sender
        :param recipient: <str> the address of recipient
        :param amount: <int> amount of sent items
        :return: <int> the index of block including this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        hash block
        :param block: <dict> block
        :return: <str> hash
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        return the last block of chain
        :return: the last block of chain
        """
        return self.chain[-1]

if __name__ == "__main__":
    blockchain = Blockchain()
    print(blockchain.new_transaction("Taro", "Jiro", 3))
    print(blockchain.current_transactions)
    print(blockchain.new_block(proof=1))