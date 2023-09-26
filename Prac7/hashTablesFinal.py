from LinkedLists import LinkedList
import csv

def next_prime(n):
    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    prime = n + 1
    while True:
        if is_prime(prime):
            return prime
        prime += 1

class DSAHashEntry:
    def __init__(self, key=None, value=None, state=0):
        self.key = key
        self.value = value
        self.state = state  # 0: Empty, 1: Occupied, 2: Deleted

class MyHashTable:
    def __init__(self, size=10007):
        self.hash_array = [DSAHashEntry() for _ in range(size)] #linked list look at this later on
        self.count = 0

    def resize(self):
        new_size = next_prime(len(self.hash_array) * 2)
        new_hash_array = [DSAHashEntry() for _ in range(new_size)]
        
        for entry in self.hash_array:
            if entry.state == 1:
                self.put(entry.key, entry.value, new_hash_array)
        
        self.hash_array = new_hash_array

    def put(self, key, value, hash_array=None):
        if hash_array is None:
            hash_array = self.hash_array

        idx = key % len(hash_array)
        new_entry = DSAHashEntry(key, value, 1)
        
        while hash_array[idx].state == 1:
            if hash_array[idx].key == key:
                hash_array[idx].value = value
                return
            idx = (idx + 1) % len(hash_array)

        hash_array[idx] = new_entry
        self.count += 1
        self.check_resize()

    def get(self, key):
        idx = key % len(self.hash_array)
        while self.hash_array[idx].state != 0:
            if self.hash_array[idx].key == key:
                return self.hash_array[idx].value
            idx = (idx + 1) % len(self.hash_array)
        return None

    def load_factor(self):
        return self.count / len(self.hash_array)

    def check_resize(self):
        if self.load_factor() > 0.7:
            self.resize()

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Key', 'Value'])
            for entry in self.hash_array:
                if entry.state == 1:
                    csv_writer.writerow([entry.key, entry.value])

    def load_from_csv(self, filename):
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                key, value = row
                self.put(int(key), value)

if __name__ == "__main__":
    hash_table = MyHashTable()
    hash_table.load_from_csv('C:\\Users\\HP\\Desktop\\RandomNames7000(1).csv')
    hash_table.save_to_csv('SavedHashTable.csv')

    # Print the entire CSV
    user_input = input("Enter 1 to print the entire CSV: ")
    if user_input == "1":
        with open('SavedHashTable.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                print(row)
    else:
        print("Invalid input")



# old code:
# import csv

# def next_prime(n):
#     def is_prime(num):
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
    
#     prime = n + 1
#     while True:
#         if is_prime(prime):
#             return prime
#         prime += 1

# class DSAHashEntry:
#     def __init__(self, key=None, value=None, state=0):
#         self.key = key
#         self.value = value
#         self.state = state  # 0: Empty, 1: Occupied, 2: Deleted

# class MyHashTable:
#     def __init__(self, size=10007):  # Increased initial size
#         self.hash_array = [DSAHashEntry() for _ in range(size)]
#         self.count = 0

#     def resize(self):
#         new_size = next_prime(len(self.hash_array) * 2)
#         new_hash_array = [DSAHashEntry() for _ in range(new_size)]
        
#         for entry in self.hash_array:
#             if entry and entry.state == 1:
#                 self.put(entry.key, entry.value, new_hash_array)
        
#         self.hash_array = new_hash_array

#     def put(self, key, value, hash_array=None):
#         if hash_array is None:
#             hash_array = self.hash_array

#         idx = key % len(hash_array)
#         new_entry = DSAHashEntry(key, value, 1)
        
#         while hash_array[idx].state == 1:
#             if hash_array[idx].key == key:
#                 hash_array[idx].value = value
#                 return
#             idx = (idx + 1) % len(hash_array)

#         hash_array[idx] = new_entry
#         self.count += 1

#     def load_factor(self):
#         return self.count / len(self.hash_array)

#     def check_resize(self):
#         lf = self.load_factor()
#         if lf > 0.7:
#             self.resize()

#     def save_to_csv(self, filename):
#         with open(filename, 'w', newline='') as csvfile:
#             csv_writer = csv.writer(csvfile)
#             csv_writer.writerow(['Key', 'Value'])
            
#             for entry in self.hash_array:
#                 if entry.state == 1:
#                     csv_writer.writerow([entry.key, entry.value])

#     def load_from_csv(self, filename):
#         with open(filename, 'r') as csvfile:
#             csv_reader = csv.reader(csvfile)
#             next(csv_reader)
            
#             for row in csv_reader:
#                 key, value = row
#                 self.put(hash(key), value)
#                 self.check_resize()



# if __name__ == "__main__":

#     hash_table = MyHashTable()
#     hash_table.load_from_csv('C:\\Users\\HP\\Desktop\\RandomNames7000(1).csv')  
#     hash_table.save_to_csv('SavedHashTable.csv')
    
# #print the entire csv
#     with open('SavedHashTable.csv', 'r') as csvfile:
#         csv_reader = csv.reader(csvfile)
#         for row in csv_reader:
#             print(row)



