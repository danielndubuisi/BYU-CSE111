from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

# test function for make_full_name
def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Jon", "Jameson") == "Jameson; Jon"
    assert make_full_name("Mary-Jane", "Hutchinson") == "Hutchinson; Mary-Jane"


# test function for make_full_name
def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Jameson; Jon") == "Jameson"
    assert extract_family_name("Hutchinson; Mary-Jane") == "Hutchinson"


# test function for make_full_name
def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Jameson; Jon") == "Jon"
    assert extract_given_name("Hutchinson; Mary-Jane") == "Mary-Jane"


# call the main function that is part of pytest so that the
# computer will execute the test functions in this file
pytest.main(["-v", "--tb=line", "-rN", __file__])
