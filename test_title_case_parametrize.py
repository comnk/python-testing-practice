from test_functions import title_case

import pytest

@pytest.mark.parametrize("sentence, expected", [
    ("hello world", "Hello World"),
    ("PyTHon TesTinG", "Python Testing"),
    ("123 testing!", "123 Testing!"),
    ("", "")
])
def test_title_case(sentence, expected):
    assert title_case(sentence) == expected

def test_title_case_error():
    with pytest.raises(TypeError):
        title_case(1234)