# agents/agent_base.py

class AgentBase:
    def __init__(self, data: dict):
        self.data = data

    def run_agent(self, county: str, zoning_code: str):
        properties = self.data.get("properties", [])
        filtered = []

        for prop in properties:
            parcel_id = prop.get("parcel_id", "").strip().upper()
            zoning = prop.get("zoning", "").strip().upper()
            county_check = county.strip().upper()
            zoning_check = zoning_code.strip().upper()

            print(f"🔍 Checking: parcel_id={parcel_id}, zoning={zoning}")

            if county_check in parcel_id and zoning.startswith(zoning_check):
                print(f"MATCHED: {parcel_id}")
                filtered.append(prop)
            else:
                print(f"SKIPPED: {parcel_id}")

        print(f"🔎 Total matched for {county} / {zoning_code}: {len(filtered)}")
        return filtered
