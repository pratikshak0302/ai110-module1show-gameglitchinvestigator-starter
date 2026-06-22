def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    #FIX: I reviewed the code and core logic was correct but output it was giving was opposite.So I changed the return statement with the help of AI and fixed it.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        # Guess is larger than the secret, so the player should aim lower.
        return "Too High", "📉 Go LOWER!"
    # Guess is smaller than the secret, so the player should aim higher.
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
