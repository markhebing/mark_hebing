import random

counter_0 = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0

seed = ("word_one", "word_two", "word_three", "word_four", "word_five", "word_six")
seed_random = list(seed)
seed_guess = list(seed)

random.shuffle(seed_random)

while counter_0 < 6 and seed_guess != seed_random:
    seed_guess[0] = seed[counter_0]
    counter_0 = counter_0 + 1
    print(seed_guess)
    counter_1 = 0
    while counter_1 < 6 and seed_guess != seed_random:
        seed_guess[1] = seed[counter_1]
        counter_1 = counter_1 + 1
        print(seed_guess)
        counter_2 = 0
        while counter_2 < 6 and seed_guess != seed_random:
            seed_guess[2] = seed[counter_2]
            counter_2 = counter_2 + 1
            print(seed_guess)
            counter_3 = 0
            while counter_3 < 6 and seed_guess != seed_random:
                seed_guess[3] = seed[counter_3]
                counter_3 = counter_3 + 1
                print(seed_guess)
                counter_4 = 0
                while counter_4 < 6 and seed_guess != seed_random:
                    seed_guess[4] = seed[counter_4]
                    counter_4 = counter_4 + 1
                    print(seed_guess)
                    counter_5 = 0
                    while counter_5 < 6 and seed_guess != seed_random:
                        seed_guess[5] = seed[counter_5]
                        counter_5 = counter_5 + 1
                        print(seed_guess)

print("Hacked!!!")
print(seed_random)
print(seed_guess)
