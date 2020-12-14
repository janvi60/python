from random_word_generator import pick_random_word

def print_current_state(current_state, attempt_remaining):
    print("current word state :", end=" ")
    for i in current_state:
        print(i, end=" ")
    print("\t\tAttempts Remaining :", attempt_remaining)


def change_state(input_char, random_word, current_state):
    modified_state = ""
    for i in range(len(random_word)):
        if current_state[i] == "_" and random_word[i] == input_char:
            modified_state += random_word[i]
        else:
            modified_state += current_state[i]
    return modified_state


def check_state(input_char, attempt_remaining, random_word, current_state):
    if input_char in random_word:
        current_state=change_state(input_char, random_word, current_state)
    else:
        attempt_remaining -=1
    
    return current_state, attempt_remaining


def check_game_status(random_word, current_state, attempt_remaining):
    if attempt_remaining <= 0:
        print("Sorry you lost")
        print("The word was", random_word)
        return True
    if current_state == random_word :
        print("congratulation you won")
        return True
    return False


random_word = pick_random_word()
current_state = ""
for i in random_word:
    if i=='a' or i=='e' or i=='o' or i=='u' or i=='i':
        current_state += i
    else:
        current_state += "_"

attempt_remaining = 5
print_current_state(current_state, attempt_remaining)

while(True):
    input_char = input("Guess the character : ")
    current_state, attempt_remaining = check_state(input_char, attempt_remaining, random_word, current_state)
    print_current_state(current_state, attempt_remaining)

    isgameover = check_game_status(random_word, current_state, attempt_remaining)
    if isgameover:
        break
