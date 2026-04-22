# Merge Dictionary and Update
# Merge Dictionary - combines two or more dictionaries into a new dictionary. it uses | or ** operator
# Update Dictionary - adds or updates key-value pairs from one dictionary to another. it uses update() method

# Example 1: Using the | operator (Python 3.9+)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2             # | operator is used to merge two dictionaries
print(merged_dict)

# Example 2: Using the ** operator

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}        # ** operator is used to merge two dictionaries
print(merged_dict)

# Example 3: Using the update() method

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)                     # update() method is used to merge two dictionaries
print(dict1)
