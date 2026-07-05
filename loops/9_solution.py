items = ["apple", "banana", "orange", "apple", "mango"]
unique_items=set()
#set takes in unique values only  duplicates are automatically removed.
#also set elements have no fixed order, so indexing like s[0] is not allowed.

for item in items:
    if item in unique_items:#second apple doesn't go into the set as it contains it duplicate
        print("Duplicate: ", item)
        break
    unique_items.add(item) 