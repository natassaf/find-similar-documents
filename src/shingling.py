class shingler:
    def __init__(self, k):
        self.shinglings_hashes = dict() # hash function is just  converting the shingle to a unique integer
        self.shingle_hash_start_number = 0
        self.k = k
    def hash_shingle(self,shingle):
        if shingle in self.shinglings_hashes:
            return self.shinglings_hashes[shingle]
        else:
            self.shinglings_hashes[shingle] = self.shingle_hash_start_number
            self.shingle_hash_start_number += 1
            return self.shingle_hash_start_number - 1
    def create_shingles(self, document): 
        shingles = set()
        for i in range(0, len(document)-self.k+1 ):
            shingles.add(self.hash_shingle(document[i:i+self.k]))
        return shingles


    def compate_sets(self,A,B):
        return len(A & B) / len(A | B)