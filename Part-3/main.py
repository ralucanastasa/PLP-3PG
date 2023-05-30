import random

"""
Write a program that counts for the user. Let the user enter the starting number, the ending number, and the amount
by which to count.
"""


def counting(start_number, end_number, step):
    if step == 0:
        print("error: impossible value for step")
        return
    elif (start_number > end_number and step > 0) or (start_number < end_number and step < 0):
        print("error: wrong counting direction")
        return
    if start_number < end_number:
        for number in range(start_number, end_number + 1, step):
            print(number)
    else:
        for number in range(start_number, end_number - 1, step):
            print(number)

"""
Create a program that gets a message from the user and then prints it out backwards.
"""


def backwards_message(message):
    new_message = message[::-1]
    print("Reversed Message:", new_message)


"""
Create a game where the computer picks a random word and the player has to guess that word. The computer tells the 
player how many letters are in the word. Then the player gets five chances to ask if a letter is in the word. The 
computer can only respond with “yes” or “no”. Then, the player must guess the word.
"""


def guess_the_word(*list_of_words):
    chosen_word = random.choice(list_of_words)
    list_of_guessed_letters = list()
    # numbers = list(range(1, 6))
    # chances = random.choice(numbers)
    chances = 5
    print("The word has", len(chosen_word), "letters and you have", chances, "chances to guess letters.")

    while chances > 0:
        letter = input("Guess a letter: ").lower()
        if letter in list_of_guessed_letters:
            print("Try a different one")
        else:
            list_of_guessed_letters.append(letter)
            chances = chances - 1

            if letter in chosen_word:
                print("Correct!")
            else:
                print("Wrong letter, try again")

    guessed_word = input("Guess the word: ").lower()

    if guessed_word == chosen_word:
        print("Correct guess!")
    else:
        print("Wrong guess! The word was:", chosen_word)


"""
Write a Python program to construct the following pattern:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""


def pattern():
    rows = 5
    for i in range(1, rows * 2):
        if i <= rows:
            print('*' * i)
        else:
            print('*' * (rows * 2 - i))


def main():
    """Ex. 1"""
    # start_number = int(input("Enter the first number: "))
    # end_number = int(input("Enter the last number: "))
    # step = int(input("Enter the step: "))
    # counting(start_number, end_number, step)

    """Ex. 2"""
    # received_message = input("Enter the message: ")
    # backwards_message(received_message)

    """Ex. 3"""
    # words = input("enter the words: ").split()
    # guess_the_word(*words)

    """Ex. 4"""
    pattern()


if __name__ == "__main__":
    main()
