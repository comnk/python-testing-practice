from functions import title_case

import pytest

def test_normal_input():
    assert title_case("hello world") == "Hello World"

def test_mixed_case():
    assert title_case("PyTHon TesTinG") == "Python Testing"

def test_number_case():
    assert title_case("123 testing!") == "123 Testing!"

def test_empty_case():
    assert title_case("") == ""

def test_title_case_error():
    with pytest.raises(TypeError):
        title_case(1234)