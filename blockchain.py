#!/usr/bin/python
# --*-- coding: utf-8 --*--
#+ Autor:	Ran#
#+ Creado:	25/05/2021 23:08:08
#+ Editado:	27/05/2021 22:46:30

from hashlib import sha256

def updatehash(*args):
    hashing_text = ''; h = sha256()
    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))

    return h.hexdigest()

class Block:
    data = None
    hash_ = None
    nonce = 0
    previous_hash = '0' * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def hash(self):
        return updatehash(self.previous_hash, self.number, self.data, self.nonce)

    def __str__(self):
        return str('Block: #{}\nHash: {}\nPrevious Hash: {}\nData: {}\nNonce: {}\n'
                .format(self.number, self.hash(), self.previous_hash, self.data, self.nonce))


class BlockChain:
    difficulty = 3

    def __init__(self, chain=[]):
        self.chain = chain

    """
    def add(self, block):
        self.chain.append({
            'hash': block.hash(), 
            'previous_hash': block.previous_hash, 
            'number': block.number, 
            'data': block.data, 
            'nonce': block.nonce
            })
    """
    def add(self, block):
        self.chain.append(block)

    def remove(self, block):
        self.chain.remove(block)

    def mine(self, block):
        try:
            #block.previous_hash = self.chain[-1].get('hash')
            block.previous_hash = self.chain[-1].hash()
        except IndexError:
            pass

        while True:
            if block.hash()[:self.difficulty] == "0"*self.difficulty:
                self.add(block)
                break
            else:
                block.nonce += 1

    def isValid(self):
        for i in range(1, len(self.chain)):
            _previous = self.chain[i].previous_hash
            _current = self.chain[i-1].hash()

            if (_previous != _current) or (_current[:self.difficulty] != '0'*self.difficulty):
                return False

        return True


def main():
    bc = BlockChain()
    database = ['ola', 'comandiamos', 'qtal', 'pene']

    num = 0
    for data in database:
        bc.mine(Block(data,num))
        num += 1

    print(bc.chain)
    for block in bc.chain:
        print(block)

    bc.chain[2].data = 'new data'
    bc.mine(bc.chain[2])
    print(bc.isValid())


if __name__ == '__main__':
    main()
