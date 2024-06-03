import pytest
from string_match import best_matches_combined


def test_best_matches_combined():
    names_dict = {
        "Oakley Sosa": "O. Sosa",
        "Francesca Dotson": "Mrs. Francesca Dotson",
        "Abel Valdez": "Abel Valdez, Phd.",
        "Yasin Rowland": "Yasin Rowland, MBA"
    }
    matches = best_matches_combined(names_dict)
    
    assert matches["Oakley Sosa"][0] == "O. Sosa"
    assert matches["Francesca Dotson"][0] == "Mrs. Francesca Dotson"
    assert matches["Abel Valdez"][0] == "Abel Valdez, Phd."
    assert matches["Yasin Rowland"][0] == "Yasin Rowland, MBA"

if __name__ == "__main__":
    pytest.main()