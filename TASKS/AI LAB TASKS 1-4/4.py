def bubble_sort(words):
    n = len(words)
    for i in range(n):
        for j in range(0, n-i-1):
            if words[j] > words[j+1]:
                words[j], words[j+1] = words[j+1], words[j]

def sort_text(input_string):
    words = input_string.split()  # Split the input string into words
    bubble_sort(words)  # Sort the words using Bubble Sort
    return ' '.join(words)  # Join the sorted words back into a string

# Example usage
input_text = "banana apple orange grape"
sorted_text = sort_text(input_text)
print("Sorted words:", sorted_text)