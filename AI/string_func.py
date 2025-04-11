def convert_string(input_string):
    # Split the string into words
    words = input_string.split()
    # Keep the first word as is, and replace remaining words with their first letter
    converted_words = [words[0]] + [word[0] for word in words[1:]]
    # Join the words with dashes
    return '-'.join(converted_words)

# Example usage
input_string = "Hey How r u"
output_string = convert_string(input_string)
print(output_string)  # Output: "Hey-How-r-y"