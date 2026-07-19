def add_item(item, shopping_list=[]):
    shopping_list.append(item)
    return shopping_list

print(add_item("apple"))  # Output: ['apple']
print(add_item("banana")) # Output: ['apple', 'banana'] (Shared state!)
