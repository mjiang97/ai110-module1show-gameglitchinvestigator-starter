from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_message_win():
    _, message = check_guess(7, 7)
    assert "Correct" in message

def test_check_guess_message_too_high():
    _, message = check_guess(80, 50)
    assert "LOWER" in message

def test_check_guess_message_too_low():
    _, message = check_guess(20, 50)
    assert "HIGHER" in message

def test_check_guess_string_secret():
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"

# --- parse_guess ---

def test_parse_guess_valid():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok is False

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert "not a number" in err.lower()

def test_parse_guess_float_string():
    ok, value, err = parse_guess("3.0")
    assert ok is True
    assert value == 3

# --- get_range_for_difficulty ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)

def test_range_unknown_defaults():
    assert get_range_for_difficulty("Unknown") == (1, 100)

# --- update_score ---

def test_update_score_win_early():
    score = update_score(0, "Win", attempt_number=1)
    assert score > 0

def test_update_score_too_low():
    score = update_score(50, "Too Low", attempt_number=3)
    assert score == 45

def test_update_score_too_high_even_attempt():
    score = update_score(50, "Too High", attempt_number=2)
    assert score == 55

def test_update_score_too_high_odd_attempt():
    score = update_score(50, "Too High", attempt_number=3)
    assert score == 45

def test_update_score_unknown_outcome():
    score = update_score(50, "Draw", attempt_number=1)
    assert score == 50
