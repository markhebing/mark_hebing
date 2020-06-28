def sentence_splitter():
    a = input("Type a sentence and I will read it backwards: ")
    b = a.split()
    b.reverse()
    print(*b)


sentence_splitter()
