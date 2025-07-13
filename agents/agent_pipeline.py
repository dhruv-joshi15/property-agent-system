# agents/agent_pipeline.py

import json
import os
from typing import Dict, Any, List

from langchain_core.runnables import RunnableLambda, RunnableSequence
from dotenv import load_dotenv
from openai import OpenAI

from agents.api_discovery_agent import discover_cook_county_api
from agents.data_extraction_agent import extract_industrial_properties
from agents.comparable_agent import load_sample_data, compute_similarity_score

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Helper: GPT-powered explanation
def explain_comparable(target: Dict[str, Any], candidate: Dict[str, Any]) -> str:
    prompt = f"""Compare two industrial properties:
Property A: {target}
Property B: {candidate}

In 2 sentences, explain why Property B is a good or bad comparable to A.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Failed to generate explanation: {str(e)}"

# Phase 1: Discovery Agent
discovery_runnable = RunnableLambda(lambda _: discover_cook_county_api())

# Phase 2: Extraction Agent
extraction_runnable = RunnableLambda(lambda _: extract_industrial_properties())

# Phase 3: Comparable Agent with GPT scoring
def run_comparables_with_gpt(_: Any) -> Dict[str, Any]:
    data = load_sample_data()
    if not data:
        return {"error": "No data loaded"}

    target = data[0]
    candidates = data[1:]

    comparables = []
    for candidate in candidates:
        score = compute_similarity_score(target, candidate)
        explanation = explain_comparable(target, candidate)
        comparables.append({
            "record": candidate,
            "score": score,
            "explanation": explanation
        })

    comparables.sort(key=lambda x: x["score"], reverse=True)
    return {
        "target": target,
        "comparables": comparables[:3]
    }

comparable_runnable = RunnableLambda(run_comparables_with_gpt)

# LangChain agent pipeline
agent_chain = RunnableSequence(
    discovery_runnable,
    extraction_runnable,
    comparable_runnable
)
