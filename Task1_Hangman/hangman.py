import random

# ========== WORD LIST ==========
WORDS = ["python", "java", "code", "alpha", "data"]

# ========== HANGMAN STAGES ==========
STAGES = [
    # 0 lives → FULL
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ---------
    """,
    # 1 life
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    ---------
    """,
    # 2 lives
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    ---------
    """,
    # 3 lives
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    # 4 lives
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    # 5 lives
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    # 6 lives → EMPTY
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """
]


# ========== HANGMAN FIGURE ==========
def draw_hangman(lives):
    print(STAGES[lives])


# ========== GAME LOOP ==========
while True:
    secret_word = random.choice(WORDS)

    display = ["_"] * len(secret_word)
    lives = 6
    guessed_letters = []
    wrong_guesses = []

    print("\n🎮 Welcome to Hangman Game!")

    while lives > 0 and "_" in display:
        draw_hangman(lives)

        print("\nWord:", " ".join(display))
        print("Lives:", lives)
        print("Wrong guesses:", wrong_guesses)

        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1:
            print("❗ Please enter exactly ONE letter!")
            continue

        if not guess.isalpha():
            print("❗ Please enter a LETTER (a-z)!")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Correct!")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display[i] = guess
        else:
            print("❌ Wrong guess!")
            lives -= 1
            wrong_guesses.append(guess)

    # ========== FINAL RESULT ==========
    draw_hangman(lives)

    if "_" not in display:
        print("\n🎉 YOU WON! The word was:", secret_word)
        print("⭐ Remaining lives:", lives)
    else:
        print("\n💀 YOU LOST! The word was:", secret_word)

    # ========== PLAY AGAIN ==========
    choice = input("\nDo you want to play again? (y/n): ").lower()
    if choice != 'y':
        print("👋 Thanks for playing!")
        break