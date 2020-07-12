def reverse_complement(sequence):
    seq = list(sequence)
    x = len(seq)
    y = 0
    while y < x:
        if seq[y] == "A":
            seq[y] = "U"
        elif seq[y] == "U":
            seq[y] = "A"
        elif seq[y] == "G":
            seq[y] = "C"
        elif seq[y] == "C":
            seq[y] = "G"
        y = y + 1
    new_seq = "".join(reversed(seq))
    print("\"" + str(new_seq) + "\"")


reverse_complement("GUGU")
reverse_complement("UCUCG")
reverse_complement("CAGGU")
