import shingling
if __name__ == "__main__":
    sh = shingling.shingler(5)
    print("starting")

    document = "This is an example document for shingling in Python."
    document2 = "This is an  document for shingling in Python."
    shingles = sh.create_shingles(document)
    shingles2 = sh.create_shingles(document2)
    print(shingles)
    print(shingles2)

    for i in range(1):
        token_1 = shingles
        for j in range(i + 1, 2):
            token_2 = shingles2
            print(token_1)
            print(token_2)
            out = sh.compate_sets(token_1,token_2)
            print(out)

