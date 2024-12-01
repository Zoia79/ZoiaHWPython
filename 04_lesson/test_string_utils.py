from mailbox import FormatError

import pytest
from StringUtils import StringUtils

def test_capitilize():
    capitilize = StringUtils()
    res = capitilize.capitilize("hello")
    assert  res == "Hello"

def test_capitilize_negative():
    capitilize = StringUtils()
    with pytest.raises(AttributeError):
            capitilize.capitilize(12345)

def test_trim():
    trim = StringUtils()
    res = trim.trim("     hello")
    assert  res == "hello"

def test_trim_no_spase():
    trim = StringUtils()
    res = trim.trim("hello")
    assert  res == "hello"

@pytest.mark.parametrize(
    'string, delimeter, result',
    [
        ("Домашка,Тренировка,Работа", ",", ["Домашка","Тренировка","Работа"]),
        ("643,-374,48.425", ",", ["643","-374","48.425"]),
        ("97l,83n,75d", ",", ["97l","83n","75d"]),
    ],
)
def test_to_list(string, delimeter, result):
    to_list = StringUtils()
    assert to_list.to_list(string, delimeter) == result

@pytest.mark.parametrize(
    'string, symbol, result',
    [
        ("Домашка", "Д", True),
        ("Домашка", "д", False),
        ("До ма шка!", "!", True),
        ("Домашка1", "1", True),
        ("Домашка", "e", False),
        ("23445", "44", True),
        ("23454", "44", False),
        ("Homework", "work", True),
    ],
)
def test_contains(string, symbol, result):
    contains = StringUtils()
    assert contains.contains(string, symbol) == result

@pytest.mark.parametrize(
        'string, symbol, result',
        [
            ("Домашка1", "1", "Домашка"),
            ("Дом ашка", " ", "Домашка"),
            ("Домашка ", " ", "Домашка"),
            ("Домашкасложно", "Домашка", "сложно"),
            ("23445", "44", "235"),
            ("23454", "44", "-"),
            ("Homework", "work", "Home"),
        ],
    )
def test_delete_symbol(string, symbol, result):
        delete_symbol = StringUtils()
        assert delete_symbol.delete_symbol(string, symbol) == result

@pytest.mark.parametrize(
    'string, symbol, result',
    [
        ("Домашка", "Д", True),
        ("Домашка", "д", False),
        (23445, 2, True),
        (23454, 24, False),
        ("Homework", "Ho", True),
        ("Homework", "To", False),
    ],
)
def test_starts_with (string, symbol, result):
    starts_with = StringUtils()
    assert starts_with.starts_with(string, symbol) == result

@pytest.mark.parametrize(
    'string, symbol, result',
    [
        ("Домашка", "а", True),
        ("Домашка", "д", False),
        (23445, 5, True),
        (23454, 34, False),
        ("Homework", "k", True),
        ("Homework", "w", False),
    ],
)
def test_end_with (string, symbol, result):
    end_with = StringUtils()
    assert end_with.end_with(string, symbol) == result

@pytest.mark.parametrize(
    'string, result',
    [
        ("", True),
        ("           ", True),
        ("Homework", False),
        ("Homework       homework", False),
        (None, True),
    ],
)
def test_is_empty (string, result):
    is_empty = StringUtils()
    assert is_empty.is_empty(string) == result

@pytest.mark.parametrize(
        'lst, joiner, result',
        [
            (["Домашка", "Тренировка", "Работа"], ",", "Домашка,Тренировка,Работа"),
            (["643", "-374", "48.45"], "+", "643+-374+48.45"),
            (["97l", "83n", "75d"], "<>", "97l<>83n<>75d"),
            ([], "/", ""),
        ],
    )
def test_list_to_string(lst, joiner, result):
        list_to_string = StringUtils()
        assert list_to_string.list_to_string(lst, joiner) == result



