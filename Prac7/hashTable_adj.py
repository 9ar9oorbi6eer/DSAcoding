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