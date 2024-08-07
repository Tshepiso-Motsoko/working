from working import convert


def test_convert():
    # Test valid time formats
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_invalid_input():
    # Test invalid time formats that should raise ValueError
    try:
        convert("9:60 AM to 5:60 PM")
        assert False, "Expected ValueError"
    except ValueError:
        pass

    try:
        convert("9 AM - 5 PM")
        assert False, "Expected ValueError"
    except ValueError:
        pass

    try:
        convert("09:00 AM - 17:00 PM")
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_am_pm_equivalence():
    # Test the equivalence of AM and PM formats
    assert convert("9 AM to 5 PM") == convert("9:00 AM to 5:00 PM")
    assert convert("10 PM to 8 AM") == convert("10:00 PM to 8:00 AM")
    assert convert("10:30 PM to 8:50 AM") == convert("10:30 PM to 8:50 AM")


if __name__ == "__main__":
    test_convert()
    test_invalid_input()
    test_am_pm_equivalence()
    print("All tests passed")
