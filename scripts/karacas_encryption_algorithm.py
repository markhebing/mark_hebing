def encrypt(user_defined_input):
    sequence = list(user_defined_input)
    sequence.reverse()
    sequence_length = len(sequence)
    x = 0
    while x < sequence_length:
        if sequence[x] == "a":
            sequence[x] = str(0)
        elif sequence[x] == "e":
            sequence[x] = str(1)
        elif sequence[x] == "i":
            sequence[x] = str(2)
        elif sequence[x] == "o":
            sequence[x] = str(2)
        elif sequence[x] == "u":
            sequence[x] = str(3)
        x = x + 1
    new_sequence = "".join(sequence)
    print("\"" + new_sequence + "aca" + "\"")


encrypt("banana")
encrypt("karaca")
encrypt("burak")
encrypt("supercalifragelisticexpialidoscious")
