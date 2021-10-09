from bank_ocr.convert_input import parse_account


def test_full_zero_entry():
    # Given
    input = """
     _  _  _  _  _  _  _  _  _ 
    | || || || || || || || || |
    |_||_||_||_||_||_||_||_||_|
    
    """

    # When
    actual = parse_account(input)

    # Then
    expected = "000000000"
    assert actual == expected
