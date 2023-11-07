import shingling
import similarities

if __name__ == "__main__":
    sh = shingling.shingler(8)
    print("starting")

    file_path = '../dataset/1.txt'
    file_path2 = '../dataset/2.txt'

    with open(file_path, 'r') as file:
        document = file.read()

    with open(file_path2, 'r') as file:
        document2 = file.read()
    
    shingles, out = sh.create_shingles(document)
    shingles2, out2 = sh.create_shingles(document2)
    document_1 = shingles
    document_2 = shingles2
    jaccard_similarity = similarities.find_jaccard_similarity(document_1, document_2)
    minhash_sim = similarities.calculate_min_hashing(document_1, document_2)


