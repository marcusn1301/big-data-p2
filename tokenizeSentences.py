# Define the sentences
Sentence_1 = "The Big Data platform for students is Blackboard"
Sentence_2 = "Questions on MinHash project by NTNU students is on Piazza"
Sentence_3 = "NTNU Big Data platform are Blackboard and Piazza"
Sentence_4 = "The project data for students are on Blackboard not Piazza"

# Combine sentences into a single string
combined_text = ' '.join([Sentence_4]).lower()

# Tokenize the text into individual words
words = combined_text.split()

# Define the parts of speech to ignore
ignored_words = {'the', 'a', 'an', 'is', 'are', 'for', 'on', 'by', 'and', 'not'}

# Custom function to create a unique list while preserving order
def unique_list(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item.lower() not in seen:
            seen.add(item.lower())
            result.append(item)
    return result

# Filter out ignored words and get unique words, converting to lowercase for case-insensitivity
unique_words = unique_list([word for word in words if word.lower() not in ignored_words])

# Sort the unique words alphabetically
unique_words_sorted = sorted(unique_words)

print(unique_words_sorted)