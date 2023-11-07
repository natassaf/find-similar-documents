import  shingling as shin

def test_shingling():
    sh = shin.shingler(10)
    print("starting")

    document = "This is an example document for shingling in Python."
    document2 = "This is a document for shingling in Python."
    shingles, out = sh.create_shingles(document)
    shingles2, out2  = sh.create_shingles(document2)
    print(list(zip(out,shingles)))
    print(list(zip(out2,shingles2)))
    for i in range(1):
        token_1 = shingles
        for j in range(i + 1, 2):
            token_2 = shingles2
            print(token_1)
            print(token_2)
            out = sh.compate_sets(token_1,token_2)
            print(out)



