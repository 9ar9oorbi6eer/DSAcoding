import unittest
from Prac7.hashTables_rough import MyHashTable

class TestMyHashTable(unittest.TestCase):
    
    def test_put(self):
        hash_table = MyHashTable()
        hash_table.put(1, "value1")
        self.assertEqual(hash_table.hash_array[1].value, "value1")
        
    def test_resize(self):
        hash_table = MyHashTable(2)
        hash_table.put(1, "value1")
        hash_table.put(2, "value2")
        hash_table.check_resize()  # This should trigger a resize
        self.assertTrue(len(hash_table.hash_array) > 2)

    def test_load_factor(self):
        hash_table = MyHashTable(10)
        hash_table.put(1, "value1")
        self.assertEqual(hash_table.load_factor(), 0.1)

    def test_save_load_csv(self):
        hash_table = MyHashTable()
        hash_table.put(1, "value1")
        hash_table.save_to_csv("temp_test.csv")

        new_hash_table = MyHashTable()
        new_hash_table.load_from_csv("temp_test.csv")
        self.assertEqual(new_hash_table.hash_array[1].value, "value1")

if __name__ == '__main__':
    unittest.main()
