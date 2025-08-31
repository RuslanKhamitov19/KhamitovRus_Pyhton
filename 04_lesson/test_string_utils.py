import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_string, expected", [
    ("  skypro", "skypro"),
])
def test_trim_positive(input_string, expected):
    assert string_utils.trim(input_string) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_string, expected", [
    ("skypro", "skypro"),
])
def test_trim_negative(input_string, expected):
    assert string_utils.trim(input_string) == expected


@pytest.mark.positive
@pytest.mark.parametrize("Input_string, symbol", [
    ("SkyPro", "S"),
])
def test_contains_positive(Input_string, symbol,):
    assert string_utils.contains(Input_string, symbol)


@pytest.mark.negative
@pytest.mark.parametrize("Input_string, symbol", [
    ("SkyPro", "U"),
])
def test_contains_negative(Input_string, symbol):
    assert not string_utils.contains(Input_string, symbol)



@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected_result", [
    ("SkyPro", "k", "SyPro"),
])
def test_delete_symbol_positive(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected_result", [
    ("SkyPro", "W", "SkyPro"),
])
def test_delete_symbol_positive(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result


