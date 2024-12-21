from address import extract_city, \
    extract_state, extract_zipcode
import pytest

# test extract_city function
def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"


# test extract_state function
def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"


# test extract_zipcode function
def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])