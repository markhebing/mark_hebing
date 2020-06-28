import random

counter_0 = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
counter_6 = 0
counter_7 = 0
counter_8 = 0
counter_9 = 0
counter_10 = 0
counter_11 = 0

seed = ("word_one", "word_two", "word_three", "word_four", "word_five", "word_six", "word_seven", "word_eight", "word_nine", "word_ten", "word_eleven", "word_twelve")
seed_random = list(seed)
seed_guess = list(seed)

random.shuffle(seed_random)

while counter_0 < 12 and seed_guess != seed_random:
    seed_guess[0] = seed[counter_0]
    counter_0 = counter_0 + 1
    print(seed_guess)
    counter_1 = 0
    while counter_1 < 12 and seed_guess != seed_random:
        seed_guess[1] = seed[counter_1]
        counter_1 = counter_1 + 1
        print(seed_guess)
        counter_2 = 0
        while counter_2 < 12 and seed_guess != seed_random:
            seed_guess[2] = seed[counter_2]
            counter_2 = counter_2 + 1
            print(seed_guess)
            counter_3 = 0
            while counter_3 < 12 and seed_guess != seed_random:
                seed_guess[3] = seed[counter_3]
                counter_3 = counter_3 + 1
                print(seed_guess)
                counter_4 = 0
                while counter_4 < 12 and seed_guess != seed_random:
                    seed_guess[4] = seed[counter_4]
                    counter_4 = counter_4 + 1
                    print(seed_guess)
                    counter_5 = 0
                    while counter_5 < 12 and seed_guess != seed_random:
                        seed_guess[5] = seed[counter_5]
                        counter_5 = counter_5 + 1
                        print(seed_guess)
                        counter_6 = 0
                        while counter_6 < 12 and seed_guess != seed_random:
                            seed_guess[6] = seed[counter_6]
                            counter_6 = counter_6 + 1
                            print(seed_guess)
                            counter_7 = 0
                            while counter_7 < 12 and seed_guess != seed_random:
                                seed_guess[7] = seed[counter_7]
                                counter_7 = counter_7 + 1
                                print(seed_guess)
                                counter_8 = 0
                                while counter_8 < 12 and seed_guess != seed_random:
                                    seed_guess[8] = seed[counter_8]
                                    counter_8 = counter_8 + 1
                                    print(seed_guess)
                                    counter_9 = 0
                                    while counter_9 < 12 and seed_guess != seed_random:
                                        seed_guess[9] = seed[counter_9]
                                        counter_9 = counter_9 + 1
                                        print(seed_guess)
                                        counter_10 = 0
                                        while counter_10 < 12 and seed_guess != seed_random:
                                            seed_guess[10] = seed[counter_10]
                                            counter_10 = counter_10 + 1
                                            print(seed_guess)
                                            counter_11 = 0
                                            while counter_11 < 12 and seed_guess != seed_random:
                                                seed_guess[11] = seed[counter_11]
                                                counter_11 = counter_11 + 1
                                                print(seed_guess)

print("Hacked!!!")
print(seed_random)
print(seed_guess)
