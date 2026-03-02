def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

def parse_guess(raw: str):
    """
    Parse the raw string entered by the user into an integer.

    Returns a tuple `(ok, value, error)` where `ok` is a boolean
    indicating whether parsing succeeded, `value` is the integer guess
    (or None), and `error` is a human-readable message if parsing failed.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        # allow floats like "3.0" to be entered
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare `guess` to `secret` and return a tuple
    `(outcome, message)`.

    Outcomes:
      * "Win"      – guess equals secret
      * "Too Low"  – guess is lower than secret
      * "Too High" – guess is higher than secret

    Hints are adjusted accordingly: if the guess is low the message
    tells the player to go higher, and vice versa.
    """
    # allow numeric strings as well as ints
    try:
        g = int(guess)
    except Exception:
        g = guess

    try:
        s = int(secret)
    except Exception:
        s = secret

    if g == s:
        return "Win", "🎉 Correct!"

    # ordering should still work for mixed types if they are comparable,
    # otherwise a TypeError will bubble up and crash – that's fine for
    # this simple game.
    if g < s:
        # guess is lower than secret
        return "Too Low", "📈 Go HIGHER!"
    else:
        # guess is greater than secret
        return "Too High", "📉 Go LOWER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
