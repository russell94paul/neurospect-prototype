from backend.llm_feedback import get_trade_feedback
import streamlit as st
import json

def enrich_trade_with_llm_feedback(trade_data: dict) -> dict:
    try:
        feedback = get_trade_feedback(trade_data)
        trade_data["llm_feedback_json"] = json.dumps(feedback)
        trade_data["llm_feedback_summary"] = feedback.get("setup_quality", "")[:100]
    except Exception as e:
        st.warning("⚠️ Failed to generate LLM feedback. Trade will be saved without it.")
        trade_data["llm_feedback_json"] = {}
        trade_data["llm_feedback_summary"] = "LLM feedback not available"
    return trade_data