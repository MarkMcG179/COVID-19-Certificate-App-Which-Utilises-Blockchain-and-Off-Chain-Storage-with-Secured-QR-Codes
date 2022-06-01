from hashlib import sha256
import json
from datetime import datetime
import time


class Block:

    def __init__(self, index, previous_hash, current_transaction, timestamp, nonce):

        self.index = index

        self.previous_hash = previous_hash

        self.current_transaction = current_transaction

        self.timestamp = timestamp

        self.nonce = nonce

        self.hash = self.compute_hash()



    def compute_hash(self):

        block_string = json.dumps(self.__dict__, sort_keys=True)

        first_hash = sha256(block_string.encode()).hexdigest()

        second_hash = sha256(first_hash.encode()).hexdigest()

        return second_hash



    def __str__(self):

        return str(self.__dict__)





class BlockChain:

    def __init__(self):

        self.chain = []

        self.transactions = []

        self.genesis_block()



    def __str__(self):

        return str(self.__dict__)



    def genesis_block(self):

        genesis_block = Block('Genesis', 0x0, [3, 4, 5, 6, 7], datetime.now().timestamp(), 0)

        genesis_block.hash = genesis_block.compute_hash()

        self.chain.append(genesis_block.hash)

        self.transactions.append(str(genesis_block.__dict__))



    def getLastBlock(self):

        return self.chain[-1]



    def proof_of_work(self, block: Block):

        difficulty = 2

        block.nonce = 0

        computed_hash = block.compute_hash()

        while not (computed_hash.endswith('0'*difficulty) and ('55'*difficulty) in computed_hash):

            block.nonce += 1

            computed_hash = block.compute_hash()

        return computed_hash



    def add(self, data):

        block = Block(len(self.chain), self.chain[-1], data, datetime.now().timestamp(), 0)

        block.hash = self.proof_of_work(block)

        self.chain.append(block.hash)

        self.transactions.append(block.__dict__)

        return json.loads(str(block.__dict__).replace('\'', '\"'))



    def getTransactions(self, id):

        labels = ['Individual_1', 'Individual_2', 'Individual_3', 'Individual_4', 'Individual_5', 'Individual_6']

        while True:

            try:

                if id == 'all':

                    for i in range(len(self.transactions)-1):

                        print('{}:\n{}\n'.format(labels[i], self.transactions[i+1]))

                    break



                elif type(id) == int:

                    return self.transactions[id]

            except Exception as e:

                print(e)
 


Individual_1 = {

            'timestamp': datetime.now(time.sleep(0.5)).timestamp(),

            'cert_id': 1,

            'data_hash' : '3d9c8832fade5f2a92f17fb5de38119dbe6aba39a3a7e19f94595de341ca1b70'

    }

Individual_2 = {

            'timestamp': datetime.now(time.sleep(0.5)).timestamp(),

            'cert_id': 2,

            'data_hash': '0af13e6f5fba123b4b535bfcf53b3017175bf15b0ac9b5e27f05f2e6cdf5676f'

    }

Individual_3 = {

            'timestamp': datetime.now(time.sleep(0.5)).timestamp(),

            'cert_id': 3,

            'data_hash': '2f009c73fdc5de27be4c2ed5a072cdd5f3980622b3d401f8e99ddb135270da60'

    }

Individual_4 = {

            'timestamp': datetime.now(time.sleep(0.5)).timestamp(),

            'cert_id': 4,

            'data_hash': '334a98a85227f9a1f85c5be913ffd8a79d4d3b0d73dd584ea082a944a684bc44'

    }

Individual_5 = {

            'timestamp': datetime.now(time.sleep(0.5)).timestamp(),

            'cert_id': 5,

            'data_hash': '3924006c0692e6d4bfa5e74634332af3e6b5ac619406af0fb6e1f39fc1ae227e'

    }

Individual_6 = {
                    
            'timestamp': datetime.now(time.sleep(0.5)).timestamp(),

            'cert_id': 6,

            'data_hash': 'f2e0f3058d228ffd3a7569ab3ea1cdd018da4f9de66587d18d1e78cc8e7324b7'

    }

B = BlockChain()

B.add(Individual_1)
B.add(Individual_2)
B.add(Individual_3)
B.add(Individual_4)
B.add(Individual_5)
B.add(Individual_6)

def main():
    B.getTransactions('all')

if __name__ == '__main__':

    main()