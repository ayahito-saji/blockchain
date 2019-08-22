# coding: UTF-8

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(selfs):
        # create new block and push chain
        pass

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
        # hash block
        pass

    @property
    def last_block(self):
        # return the last block of chain
        pass
