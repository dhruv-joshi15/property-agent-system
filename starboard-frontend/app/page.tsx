'use client';

import { useState } from 'react';
import { fetchComparables } from '@/lib/modelService';

export default function Home() {
  const [county, setCounty] = useState('DALLAS');
  const [parcelId, setParcelId] = useState('');
  const [comparables, setComparables] = useState<any[]>([]);
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    setError('');
    setComparables([]);
    try {
      const data = await fetchComparables(county, parcelId);
      setComparables(data.comparables);
    } catch (err) {
      setError('Failed to fetch comparables. Please check the Parcel ID.');
    }
  };

  return (
    <main className="min-h-screen bg-gradient-to-b from-black via-gray-900 to-blue-950 flex items-center justify-center p-6">
      <div className="w-full max-w-2xl text-center">
        <h1 className="text-2xl md:text-3xl font-bold text-white mb-8">
          Starboard Property Comparables
        </h1>

        <div className="space-y-4 mb-6">
          <select
            className="w-full p-3 rounded-md bg-gray-800 text-white focus:outline-none"
            value={county}
            onChange={(e) => setCounty(e.target.value)}
          >
            <option value="DALLAS">DALLAS</option>
            <option value="COOK">COOK</option>
            <option value="LA">LA</option>
          </select>

          <input
            type="text"
            placeholder="Enter Parcel ID"
            value={parcelId}
            onChange={(e) => setParcelId(e.target.value)}
            className="w-full p-3 rounded-md bg-gray-800 text-white focus:outline-none"
          />

          <button
            onClick={handleSubmit}
            className="w-full p-3 bg-blue-600 hover:bg-blue-700 rounded-md text-white font-semibold transition"
          >
            Fetch Comparables
          </button>
        </div>

        {error && <p className="text-red-500 mb-4">{error}</p>}

        <div className="mt-8 space-y-4 text-left animate-fadeIn">
          {comparables.map((comp, index) => (
            <div
              key={index}
              className="bg-gray-800 p-5 rounded-xl shadow-md border border-gray-700 transition-transform transform hover:scale-[1.01]"
            >
              <p className="font-semibold">
                <span className="text-gray-300">Parcel ID:</span>{' '}
                <code className="font-mono">{comp.parcel_id}</code>
              </p>
              <p>
                <span className="text-gray-300">Zoning:</span> {comp.zoning}
              </p>
              <p>
                <span className="text-gray-300">Shape Area:</span> {comp.shape_area}
              </p>
              <p>
                <span className="text-gray-300">Location:</span> {comp.location}
              </p>
              <p>
                <span className="text-gray-300">Building Age:</span> {comp.building_age}
              </p>
              <p>
                <span className="text-gray-300">Similarity Score:</span>{' '}
                <span
                  className={
                    comp.similarity_score > 0.25
                      ? 'text-green-400 font-bold'
                      : comp.similarity_score > 0.1
                      ? 'text-yellow-400 font-bold'
                      : 'text-red-400 font-bold'
                  }
                >
                  {comp.similarity_score.toFixed(3)}
                </span>
              </p>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
