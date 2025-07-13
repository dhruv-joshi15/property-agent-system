# agents/comparable_agent.py

from data.properties import PROPERTY_DATA as PROPERTIES_DATA
from typing import List, Dict
import math

def is_industrial(zoning: str) -> bool:
    zoning = zoning.upper()
    return any(zone in zoning for zone in ["M1", "M2", "I-1", "I-2"])

def calculate_similarity_score(target, other) -> float:
    # Size difference (normalized)
    size_diff = abs(target["shape_area"] - other["shape_area"]) / max(target["shape_area"], 1)

    # Age difference
    age_diff = abs(target["building_age"] - other["building_age"]) / max(target["building_age"], 1)

    # Location match (rough string comparison)
    loc_match = target["location"].split(",")[-1].strip() == other["location"].split(",")[-1].strip()
    location_score = 0 if loc_match else 1

    # Weighted score (lower is better)
    return round(size_diff * 0.4 + age_diff * 0.4 + location_score * 0.2, 3)

def get_comparables(target_id: str, top_k: int = 3) -> List[Dict]:
    target = next((p for p in PROPERTIES_DATA if p["parcel_id"] == target_id), None)
    if not target or not is_industrial(target["zoning"]):
        return []

    candidates = [
        p for p in PROPERTIES_DATA
        if p["parcel_id"] != target_id and is_industrial(p["zoning"])
    ]

    scored = [
        {**p, "similarity_score": calculate_similarity_score(target, p)}
        for p in candidates
    ]

    return sorted(scored, key=lambda x: x["similarity_score"])[:top_k]
