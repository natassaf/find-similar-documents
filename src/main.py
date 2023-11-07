import shingling
import similarities
 
if __name__ == "__main__":
    sh = shingling.shingler(8)
    print("starting")

    # document = "This is an example document for shingling in Python."
    # document2 = "This is an  document for shingling in Python."
    # Specify the file path
    file_path = '../dataset/1.txt'

    file_path2 = '../dataset/2.txt'

    with open(file_path, 'r') as file:
        document = file.read()

    with open(file_path2, 'r') as file:
        document2 = file.read()

    
    shingles, out = sh.create_shingles(document)
    shingles2, out2  = sh.create_shingles(document2)
    print(list(zip(out,shingles)))
    print(list(zip(out2,shingles2)))
    # print(out)
    # print(out2)
    # print(shingles)
    # print(shingles2)

    for i in range(1):
        token_1 = shingles
        for j in range(i + 1, 2):
            token_2 = shingles2
            print(token_1)
            print(token_2)
            out = similarities.find_jaccard_similarity(token_1,token_2)
            print(out)

