# Empty list 
my_list = []

# Appending elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"After appending: {my_list}")

# Inserting 15 at the 2nd position 
my_list.insert(1, 15)
print(f"After inserting 15 at position 2: {my_list}")

# Extending with another list
my_list.extend([50, 60, 70])
print(f"After extending with [50, 60, 70]: {my_list}")

# Removing the last element
my_list.pop()
print(f"After removing last element: {my_list}")

# Sorting in ascending order
my_list.sort()
print(f"After sorting: {my_list}")

# Finding and printing the index of 30
index_30 = my_list.index(30)
print(f"Index of value 30: {index_30}")
