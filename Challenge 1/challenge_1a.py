def compress(s):
    if not s:
        return s  # Return empty string if input is empty

    compressed = []  # List to store compressed characters and counts
    current_char = s[0]  # Initialize with the first character
    count = 1  # Initialize the count of the current character

    # Iterate through the string from the second character onwards
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1  # Increment the count if the character is the same as the current character
        else:
            compressed.append(
                current_char + str(count)
            )  # Append compressed character and count

            current_char = s[i]  # Update the current character
            count = 1  # Reset the count for the new character

    # Append the last character and its count
    compressed.append(current_char + str(count))

    # Join the compressed characters and counts to form the compressed string
    compressed_str = "".join(compressed)

    # Return the shorter of the original and compressed strings
    return compressed_str if len(compressed_str) < len(s) else s


# Running Test cases
assert compress("bbcceeee") == "b2c2e4"
assert compress("aaabbbcccaaa") == "a3b3c3a3"
assert compress("a") == "a"


"""
The time complexity of the provided string compression algorithm is O(n), where 'n' represents the length of the input string.
It performs a single loop through the input string, appending characters and counts to a list, and then joining them into the final compressed string.
Other operations like appending to the list and joining the characters are typically O(1) or O(k), where k is the length of the resulting compressed string, 
and do not significantly impact the overall time complexity.
"""
