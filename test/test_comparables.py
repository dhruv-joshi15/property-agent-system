from agents.comparable_agent import find_comparables

def test_valid_parcel():
    result = find_comparables("123456789")
    assert "comparables" in result
    assert isinstance(result["comparables"], list)