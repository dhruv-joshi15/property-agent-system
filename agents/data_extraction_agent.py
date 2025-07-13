import json
from pathlib import Path

def extract_industrial_properties():
    data_path = Path("data/cook_county_sample.json")
    with open(data_path, "r") as f:
        data = json.load(f)

    # Industrial zoning codes
    industrial_codes = {"M1", "M1-1", "M2", "M2-2", "I-1", "I-2"}

    filtered = []
    for record in data:
        zoning = record.get("zoning_class", "").upper()
        if any(code in zoning for code in industrial_codes):
            filtered.append(record)

    return {
        "total_properties": len(data),
        "industrial_properties": len(filtered),
        "sample_industrial": filtered[0] if filtered else None
    }

if __name__ == "__main__":
    print(extract_industrial_properties())
