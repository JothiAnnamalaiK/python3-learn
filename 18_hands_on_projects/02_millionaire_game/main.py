import random

questions = [
    ["What is the capital of France?", ["paris", "london", "berlin", "madrid"], 0],
    [
        "What is the largest planet in our solar system?",
        ["earth", "jupiter", "mars", "venus"],
        1,
    ],
    ["What is the chemical symbol for water?", ["h2o", "co2", "o2", "n2"], 0],
    [
        "Who wrote 'Romeo and Juliet'?",
        ["william shakespeare", "charles dickens", "jane austen", "mark twain"],
        0,
    ],
    ["What is the smallest prime number?", ["1", "2", "3", "5"], 1],
    ["What is the currency of Japan?", ["yen", "dollar", "euro", "pound"], 0],
    [
        "Who painted the Mona Lisa?",
        ["leonardo da vinci", "vincent van gogh", "pablo picasso", "claude monet"],
        0,
    ],
    [
        "What is the largest mammal?",
        ["elephant", "blue whale", "giraffe", "hippopotamus"],
        1,
    ],
    ["What is the chemical symbol for gold?", ["au", "ag", "fe", "cu"], 0],
    [
        "Who is the author of the Harry Potter series?",
        ["j.k. rowling", "stephen king", "george r.r. martin", "agatha christie"],
        0,
    ],
]

prizes = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000]


shuffle_questions = True
shuffle_options = True


def play_game():
    score = 0
    prizes_won = []
    game_questions = questions[:]

    if shuffle_questions:
        random.shuffle(game_questions)

    for i, (question, options, correct_index) in enumerate(game_questions):
        if shuffle_options:
            shuffled_options = options[:]
            random.shuffle(shuffled_options)
            correct_index = shuffled_options.index(options[correct_index])
        else:
            shuffled_options = options

        print(f"Question {i + 1}: {question}")
        for j, option in enumerate(shuffled_options):
            print(f"{j + 1}. {option}")
        answer = get_valid_answer(len(shuffled_options))
        if answer == correct_index:
            print("Correct!")
            score += 1
            prizes_won.append(prizes[i])
            print(f"You won: ${prizes[i]}")
        else:
            print(f"Wrong! The correct answer is: {shuffled_options[correct_index]}")
    print(f"Your final score is: {score}/{len(game_questions)}")
    if prizes_won:
        print(f"You won the following prizes: {', '.join(str(p) for p in prizes_won)}")
        print(f"Total prize money won: ${sum(prizes_won)}")
    else:
        print("You did not win any prizes. Better luck next time!")


def get_valid_answer(num_options):
    while True:
        try:
            answer = int(input("Enter the number of your answer: ")) - 1
            if 0 <= answer < num_options:
                return answer
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    print("Welcome to the Millionaire Game!")
    play_game()
