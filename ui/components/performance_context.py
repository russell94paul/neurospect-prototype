import streamlit as st

def performance_context_ui():
    st.markdown("## 📊 Performance Context & Mindset")

    account_type = st.selectbox("Account Type", ["Evaluation", "Funded", "Payout Phase", "Demo"])
    drawdown_proximity = st.selectbox("Drawdown Proximity", ["No drawdown", "25%", "50%", "75%", "At limit"])
    eval_progress = st.selectbox("Evaluation Progress", ["Start", "25%", "50%", "75%", "Close to pass"])
    days_left = st.number_input("Days Left in Evaluation", min_value=0, step=1)
    payout_proximity = st.selectbox("Payout Proximity", ["Just started", "2+ weeks", "Next week", "This week"])
    sleep_quality = st.selectbox("Did you sleep well?", ["Yes", "Somewhat", "Poorly"])
    caffeine = st.selectbox("Caffeine Intake", ["None", "Low", "Normal", "High"])
    distractions = st.selectbox("Distractions while trading?", ["None", "Some", "High"])
    emotional_regulation = st.checkbox("Emotional Regulation Protocol (Meditation / Gym / Mindset Podcast etc.)")
    routine_done = st.checkbox("Followed routine?")
    reviewed_plan = st.checkbox("Reviewed playbook before session?")
    bias_prepped = st.checkbox("Had a pre-session bias?")
    risk_today = st.selectbox("Risk per trade today", ["Full", "Half", "Micro", "Over-risked"])
    matches_plan = st.selectbox("Trade matches strategy?", ["Yes", "Partial", "No"])
    setup_grade = st.selectbox("Setup Grade", ["A+", "A", "B", "C"])
    prep_time = st.selectbox("Prep Time Before Trading", ["None", "<15m", "15–30m", "30+m"])

    return {
        "account_type": account_type,
        "drawdown_proximity": drawdown_proximity,
        "eval_progress": eval_progress,
        "days_left": days_left,
        "payout_proximity": payout_proximity,
        "sleep_quality": sleep_quality,
        "caffeine": caffeine,
        "distractions": distractions,
        "emotional_regulation": emotional_regulation,
        "routine_done": routine_done,
        "reviewed_plan": reviewed_plan,
        "bias_prepped": bias_prepped,
        "risk_today": risk_today,
        "matches_plan": matches_plan,
        "setup_grade": setup_grade,
        "prep_time": prep_time,
    }
