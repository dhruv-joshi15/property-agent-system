# Starboard Agent System

The Starboard Agent System is a multi-agent platform for discovering and comparing industrial properties across different counties. It includes a FastAPI backend powered by LangChain agents, and a Next.js frontend for user interaction.

## Features

- API discovery based on selected county
- Data extraction for industrial properties
- GPT-powered explanation of comparable properties
- Modular LangChain agent pipeline
- User-friendly frontend with parcel ID input

## Tech Stack

- **Backend:** FastAPI, Python, LangChain, OpenAI API
- **Frontend:** Next.js 14, TailwindCSS, TypeScript

## Sample Parcel IDs

- **Cook County:** `COOK001`
- **Dallas County:** `DALLAS123`
- **Los Angeles County:** `LA999`

## Backend Setup (FastAPI)

```bash
# Navigate to project root
cd starboard-agent-system

# Create and activate virtual environment (optional)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "OPENAI_API_KEY=your_openai_key_here" > .env

# Start the FastAPI server
uvicorn main:app --reload --port 5002


Server will run at: http://localhost:5002


Frontend Setup (Next.js) -

# Navigate to frontend folder
cd starboard-frontend

# Install frontend dependencies
npm install

# Set API base URL for frontend
echo "NEXT_PUBLIC_API_URL=http://localhost:5002" > .env.local

# Start the development server
npm run dev -- -p 3001

App will be available at: http://localhost:3001


starboard-agent-system/
├── agents/                 # All LangChain agents
├── data/                   # Sample property data
├── starboard-frontend/     # Next.js frontend app
├── test/                   # Tests (optional)
├── main.py                 # FastAPI entry point
├── requirements.txt        # Backend dependencies


How It Works
User selects a county and enters a parcel ID in the frontend.

Frontend sends a POST request to /api/<county>/properties.

Backend runs a pipeline of agents:

API Discovery

Data Extraction

Comparable Computation

GPT-based Explanation

A short explanation of comparable properties is returned.


