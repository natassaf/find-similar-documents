

def find_jaccard_similarity(A,B):
    return len(A & B) / len(A | B)

def calculate_min_hashing(document_1, document_2):
    return 1