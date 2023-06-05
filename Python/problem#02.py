import collections 

def are_all_values_same(string):
    dictionary = collections.Counter(string)
    # Get the first value of the dictionary
    first_value = dictionary[list(dictionary.keys())[0]]

    # Check if all the values in the dictionary are equal to the first value
    return all(value == first_value for value in dictionary.values())

# Test case 1
string = 'abc'
expected_output = True

# Actual output
actual_output = are_all_values_same(string)

# Check if the actual output is equal to the expected output
assert actual_output == expected_output 

# Test case 2
string = 'abcc'
expected_output = False

# Actual output
actual_output = are_all_values_same(string)

# Check if the actual output is equal to the expected output
assert actual_output == expected_output 