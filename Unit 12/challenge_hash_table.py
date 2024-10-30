class HashTable:
    def __init__(self, size):
        # Initialize the hash table with a specified size
        self.size = size
        # Create a list of empty lists for each index to handle collisions using chaining
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # Private helper function to compute the hash index of a key
        return hash(key) % self.size

    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        index = self._hash(key)  # Calculate the hash index for the key
        bucket = self.table[index]  # Access the list (bucket) at the computed index
        for i, (k, v) in enumerate(bucket):
            # If the key already exists in the bucket, update its value
            if k == key:
                bucket[i] = (key, value)
                return
        # If key does not exist in the bucket, append the new key-value pair
        bucket.append((key, value))

    def get(self, key):
        # Retrieve the value associated with a key
        index = self._hash(key)  # Calculate the hash index for the key
        bucket = self.table[index]  # Access the list (bucket) at the computed index
        for k, v in bucket:
            # Search through the bucket for the key
            if k == key:
                return v  # Return the value if found
        return None  # Return None if the key is not found

    def delete(self, key):
        # Delete a key-value pair from the hash table
        index = self._hash(key)  # Calculate the hash index for the key
        bucket = self.table[index]  # Access the list (bucket) at the computed index
        for i, (k, v) in enumerate(bucket):
            # Search through the bucket for the key
            if k == key:
                del bucket[i]  # Remove the key-value pair if found
                return True  # Return True indicating successful deletion
        return False  # Return False if the key is not found

    def print_table(self):
        # Print each index and its corresponding bucket in the hash table
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")  # Display each bucket in the hash table


# Create a hash table with a small size to force collisions
hash_table = HashTable(5)


# Insert some key-value pairs
print("Inserting values...")
hash_table.insert("apple", 5)    # Insert "apple" with value 5
hash_table.insert("banana", 3)   # Insert "banana" with value 3
hash_table.insert("grape", 8)    # Insert "grape" with value 8
print("\n---\n")

# Retrieve values
print("Retrieving values...")
print(f"Get 'apple': {hash_table.get('apple')}")    # Retrieve the value for "apple"
print(f"Get 'banana': {hash_table.get('banana')}")  # Retrieve the value for "banana"
print(f"Get 'grape': {hash_table.get('grape')}")    # Retrieve the value for "grape"
print("\n---\n")

# Print the current hash table
print("Current hash table:")
hash_table.print_table()  # Display the current structure of the hash table
print("\n---\n")

# Delete a value and verify deletion
print("Deleting 'banana'...")
hash_table.delete("banana")  # Delete "banana" from the hash table
hash_table.print_table()     # Print the hash table to confirm deletion
