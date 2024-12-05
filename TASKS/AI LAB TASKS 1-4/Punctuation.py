def remove_punctuation(input_string):
    result = ""
    for char in input_string:
        if char.isalnum() or char.isspace():
            result += char
    return result

# Get user input
user_input = input("Enter a string: ")
cleaned_string = remove_punctuation(user_input)
print("String without punctuation:", cleaned_string)
