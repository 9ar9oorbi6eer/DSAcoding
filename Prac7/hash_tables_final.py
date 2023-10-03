from LinkedLists import *
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

class MyHashTable:
    def __init__(self, size=3):
        self.bucket_count = size
        self.buckets = [DSALinkedList() for _ in range(size)]
        self.count = 0

    def resize(self):
        new_size = next_prime(self.bucket_count * 2)
        new_buckets = [DSALinkedList() for _ in range(new_size)]
        
        for bucket in self.buckets:
            current = bucket.head
            while current:
                key_val = current.getValue()
                hash_value = hash(key_val.key) % new_size
                new_buckets[hash_value].insertLast(DSAHashEntryKeyValue(key_val.key, key_val.value))
                current = current.getNext()

        self.bucket_count = new_size
        self.buckets = new_buckets

    def put(self, key, value):
        hash_value = hash(key) % self.bucket_count
        bucket = self.buckets[hash_value]
        existing_entry = bucket.findByKey(key)
        
        if existing_entry:
            existing_entry.value = value
        else:
            bucket.insertLast(DSAHashEntryKeyValue(key, value))
            self.count += 1
            self.check_resize()

    def get(self, key):
        hash_value = hash(key) % self.bucket_count
        bucket = self.buckets[hash_value]
        entry = bucket.findByKey(key)
        return entry.value if entry else None

    def load_factor(self):
        return self.count / self.bucket_count

    def check_resize(self):
        if self.load_factor() > 0.7:
            self.resize()

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Key', 'Value'])
            for bucket in self.buckets:
                current = bucket.head
                while current:
                    key_val = current.getValue()
                    csv_writer.writerow([key_val.key, key_val.value])
                    current = current.getNext()

    def load_from_csv(self, filename):
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                key, value = row
                self.put(int(key), value)

    def remove(self, key):
        hash_value = hash(key) % self.bucket_count
        bucket = self.buckets[hash_value]
        removed = bucket.removeByKey(key)
        if removed:
            self.count -= 1
        return None if not removed else key

if __name__ == "__main__":
    hash_table = MyHashTable()
    
    hash_table.put(1, "John")
    hash_table.put(2, "Mary")
    hash_table.put(3, "Bob")
    hash_table.put(4, "Jane")
    hash_table.put(5, "Peter")
    hash_table.put(6, "Sarah")
    print(hash_table.count)
    hash_table.remove(1)
    hash_table.remove(2)
    hash_table.remove(3)
    hash_table.remove(4)
    print(hash_table.count)
    hash_table.load_from_csv('C:\\Users\\HP\\Desktop\\RandomNames7000(1).csv')
    hash_table.save_to_csv('SavedHashTable.csv')

    user_input = input("Enter 1 to print the entire CSV: ")
    if user_input == "1":
        with open('SavedHashTable.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                print(row)
    else:
        print("Invalid input")
    
    print(hash_table.count)
    print(f"duplicates are:", 7000 - hash_table.count)





# from LinkedLists import *
# import csv
# import numpy as np


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
#     def __init__(self):
#         self.linkedList = DSALinkedList()

        
# class MyHashTable:
#     def __init__(self, size=3):
#         self.bucket_count = size
#         self.buckets = [DSALinkedList() for _ in range(size)]
#         self.count = 0
# # class MyHashTable:
# #     def __init__(self, size=3):
# #         self.hash_array = np.array([DSAHashEntry() for _ in range(size)], dtype=object)
# #         self.count = 0

#     def resize(self):
#         new_size = next_prime(len(self.hash_array) * 2)
#         new_hash_array = [DSAHashEntry() for _ in range(new_size)]
        
#         for old_entry in self.hash_array:
#             current = old_entry.linkedList.head
#             while current:
#                 key_val = current.getValue()
#                 self.put_into_specific_array(key_val.key, key_val.value, new_hash_array)
#                 current = current.getNext()

#         self.hash_array = new_hash_array

#     def put_into_specific_array(self, key, value, hash_array):
#         idx = key % len(hash_array)
#         existing_entry = hash_array[idx].linkedList.findByKey(key)
        
#         if existing_entry:
#             existing_entry.value = value
#         else:
#             hash_array[idx].linkedList.insertLast(DSAHashEntryKeyValue(key, value))

                

#     def put(self, key, value):
#         hash_value = hash(key) % self.bucket_count
#         bucket = self.buckets[hash_value]
#         bucket.insertLast(DSAHashEntryKeyValue(key, value))
#         self.count += 1

#     def get(self, key):
#         hash_value = hash(key) % self.bucket_count
#         bucket = self.buckets[hash_value]
#         entry = bucket.findByKey(key)
#         return entry.value if entry else None

#     # def put(self, key, value, hash_array=None):
#     #     if hash_array is None:
#     #         hash_array = self.hash_array

#     #     idx = key % len(hash_array)
#     #     new_entry = DSAHashEntry(key, value, 1)
        
#     #     while hash_array[idx]. == 1:
#     #         if hash_array[idx].key == key:
#     #             hash_array[idx].value = value
#     #             return
#     #         idx = (idx + 1) % len(hash_array)

#     #     hash_array[idx] = new_entry
#     #     self.count += 1
#     #     self.check_resize()

#     # def get(self, key):
#     #     idx = key % len(self.hash_array)
#     #     while self.hash_array[idx]. != 0:
#     #         if self.hash_array[idx].key == key:
#     #             return self.hash_array[idx].value
#     #         idx = (idx + 1) % len(self.hash_array)
#     #     return None



#     def load_factor(self):
#         return self.count / len(self.hash_array)

#     def check_resize(self):
#         if self.load_factor() > 0.7:
#             self.resize()
            
#     def save_to_csv(self, filename):
#         with open(filename, 'w', newline='') as csvfile:
#             csv_writer = csv.writer(csvfile)
#             csv_writer.writerow(['Key', 'Value'])
#             for entry in self.hash_array:
#                 current = entry.linkedList.head
#                 while current:
#                     key_val = current.getValue()
#                     csv_writer.writerow([key_val.key, key_val.value])
#                     current = current.getNext()


#     # def save_to_csv(self, filename):
#     #     with open(filename, 'w', newline='') as csvfile:
#     #         csv_writer = csv.writer(csvfile)
#     #         csv_writer.writerow(['Key', 'Value'])
#     #         for entry in self.hash_array:
#     #             if entry == 1:
#     #                 csv_writer.writerow([entry.key, entry.value])

#     def load_from_csv(self, filename):
#         with open(filename, 'r') as csvfile:
#             csv_reader = csv.reader(csvfile)
#             next(csv_reader)
#             for row in csv_reader:
#                 key, value = row
#                 self.put(int(key), value)
                
#     def remove(self, key):
#         idx = key % len(self.hash_array)
#         removed = self.hash_array[idx].linkedList.removeByKey(key)
#         if removed:
#             self.count -= 1
#         return None if not removed else key

#     # def remove(self, key):
#     #     idx = key % len(self.hash_array)
#     #     while self.hash_array[idx]. != 0:
#     #         if self.hash_array[idx].key == key:
#     #             self.hash_array[idx]. = 2
#     #             self.count -= 1
#     #             return
#     #         idx = (idx + 1) % len(self.hash_array)
#     #     return None

# if __name__ == "__main__":
#     hash_table = MyHashTable()
    
#     hash_table.put(1, "John")
#     hash_table.put(2, "Mary")
#     hash_table.put(3, "Bob")
#     hash_table.put(4, "Jane")
#     hash_table.put(5, "Peter")
#     hash_table.put(6, "Sarah")
#     print(hash_table.count)
#     hash_table.remove(1)
#     hash_table.remove(2)
#     hash_table.remove(3)
#     hash_table.remove(4)
#     print(hash_table.count)
#     hash_table.load_from_csv('C:\\Users\\HP\\Desktop\\RandomNames7000(1).csv')
#     hash_table.save_to_csv('SavedHashTable.csv')

#     user_input = input("Enter 1 to print the entire CSV: ")
#     if user_input == "1":
#         with open('SavedHashTable.csv', 'r') as csvfile:
#             csv_reader = csv.reader(csvfile)
#             for row in csv_reader:
#                 print(row)
#     else:
#         print("Invalid input")
    
#     print(hash_table.count)
#     print(f"duplicates are:", 7000 - hash_table.count)
