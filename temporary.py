# Jaccard similarity
def jaccard_similarity(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    intersection = len(s1.intersection(s2))
    union = len(s1.union(s2))
    return intersection / union if union != 0 else 0


sentences = [Sentence_1, Sentence_2, Sentence_3, Sentence_4]
sim_matrix = []
max_similarity = 0
max_pair = []
for _ in range(len(sentences)):
    sim_matrix.append([])

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        similarity_value = jaccard_similarity(sentences[i], sentences[j])
        sim_matrix[i].append([[i,j],similarity_value])
        if similarity_value > max_similarity:
            max_similarity = similarity_value
            max_pair = [i,j]



print("Jaccard Similarity Matrix:")
print(sim_matrix)
print("\n")

print(f"The two most similar sentences are sentence {max_pair[0]+1} and sentence {max_pair[1]+1}, with a similarity of {max_similarity}.")