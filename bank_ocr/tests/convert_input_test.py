from convert_input import _parse_digit
import pytest

digit_test_data = [
    (
        """
         _ 
        | |
        |_|
        
        """,
        '0'
    ),
    (
        """
        
          |
          |
        
        """,
        '1'
    ),
    (
        """
         _  
         _|
        |_ 
        
        """,
        '2'
    ),
    (
        """
         _ 
         _|
         _|
        
        """,
        '3'
    ),
    (
        """
        
        |_|
          |
        
        """,
        '4'
    ),
    (
        """
         _  
        |_  
         _|
        
        """,
        '5'
    ),
    (
        """
         _ 
        |_  
        |_|
        
        """,
        '6'
    ),
    (
        """
         _ 
          |
          |

        """,
        '7'
    ),
    (
        """
         _ 
        |_|
        |_|
        
        """,
        '8'
    ),
    (
        """
         _ 
        |_|
         _|
        
        """,
        '9'
    ),
]


@pytest.mark.parametrize('input_digit,expected', digit_test_data)
def test_parse_one_digit(input_digit, expected):
    # Given
    # When
    actual = _parse_digit(digit_str=input_digit)

    # Then
    assert actual == expected
