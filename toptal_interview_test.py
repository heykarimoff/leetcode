import toptal_interview as interview
import math
import pytest


def test_truncate_words():
    assert (
        interview.truncate_words("Hello how are you Contestant", 4)
        == "Hello how are you"
    )
    assert (
        interview.truncate_words("Hello! how are you? Are you Contestant.", 4)
        == "Hello! how are you?"
    )


def test_truncate_sentence():
    assert (
        interview.truncate_sentence("Hello how are you Contestant", 4)
        == "Hello how are you"
    )


def test_allocate_people_to_seats():
    assert interview.allocate_people_to_seats([3, 1, 2], [4, 5, 2]) == 2


def test_factory_filters():
    assert interview.factory_filters([5, 19, 8, 1]) == 3
    assert interview.factory_filters([10, 10]) == 2
    assert interview.factory_filters([3, 0, 5]) == 2


def test_factory_filters_recursive():
    assert interview.factory_filters_recursive([5, 19, 8, 1], 16.5) == 3
