class DSAHashEntry:
    def __init__(self, key = "", value = None, state = 0):
        self.key = key
        self.value = value
        self.state = state  

class DSAHashTable:
    def __init__(self, table_size):
        self.count = 0
        self.hash_array = [DSAHashEntry() for _ in range(table_size)]

    def get(self, in_key):
        hash_idx = self.hash(in_key)
        step_size = self.second_hash(in_key)  
        orig_idx = hash_idx
        found = False
        give_up = False

        while not found and not give_up:
            if self.hash_array[hash_idx].state == 0:
                give_up = True
            elif self.hash_array[hash_idx].key == in_key:
                found = True
            else:
                hash_idx = (hash_idx + step_size) % len(self.hash_array)  
                if hash_idx == orig_idx:
                    give_up = True

        if not found:
            raise KeyError(f"Key {in_key} not found in hash table.")

        return self.hash_array[hash_idx].value

    def hash(self, key):
        return hash(key) % len(self.hash_array)

    def second_hash(self, key):
        return (5 - (hash(key) % 5))  