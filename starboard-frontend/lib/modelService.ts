const baseUrl = process.env.NEXT_PUBLIC_API_URL as string;

export const fetchComparables = async (county: string, parcelId: string) => {
  const url = `${baseUrl}/api/${county.toLowerCase()}/properties`;
  const res = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ parcel_id: parcelId }),
  });

  if (!res.ok) {
    throw new Error("Failed to fetch comparables");
  }

  const data = await res.json();
  return data;
};
