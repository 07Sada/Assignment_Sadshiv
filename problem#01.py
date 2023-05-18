import collections

def frequent_word(string):
    counter = collections.Counter(string.split())
    most_frequent_word = counter.most_common(1)[0][0]

    # Print the most frequent word
    print(f"Most frequent word in the string: {most_frequent_word}")
    print(f"Length of the most frequent word: {len(most_frequent_word)}\n")
    return len(most_frequent_word)

string = "write write write all the number from from from 1 to 100"
frequent_word(string=string)

# Test cases

# Test case 1
string1 = "The quick brown fox jumps over the lazy dog."
expected_length = 3

# Actual length
actual_length = frequent_word(string1)

# Check if the actual length is equal to the expected length
assert actual_length == expected_length, "Actual length not equal to expected length."

# Test case 2
string2 = "apple apple orange orange orange"
expected_length = 6

# Actual length
actual_length = frequent_word(string2)

# Check if the actual length is equal to the expected length
assert actual_length == expected_length, "Actual length not equal to expected length."