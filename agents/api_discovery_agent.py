import json
from pathlib import Path

def discover_cook_county_api():
    data_path = Path("data/cook_county_sample.json")
    with open(data_path, "r") as f:
        data = json.load(f)

    sample = data[0]

    field_mappings = {
        "square_feet": ["shape_area", "building_sqft", "sqft"],
        "zoning_class": ["zoning_class", "zoning"],
        "address": ["location", "site_address"]
    }

    return {
        "sample_record": sample,
        "normalized_fields": field_mappings
    }

if __name__ == "__main__":
    output = discover_cook_county_api()
    print("Discovered:", output)
