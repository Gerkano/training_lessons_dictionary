import random, string

def dict_generator() -> str:
    my_dictionary = {}

    while True:
        random_letter = random.choice(string.ascii_lowercase)
        random_number = random.randint(1, 30)

        if random_number not in my_dictionary.values():
            my_dictionary[random_letter] = random_number

        if len(my_dictionary) >= 10:
            break
    print(my_dictionary)   
    return max(my_dictionary, key=my_dictionary.get)


      
print(dict_generator())