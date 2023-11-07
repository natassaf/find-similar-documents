def find_jaccard_similarity(A,B):
    return len(A & B) / len(A | B)