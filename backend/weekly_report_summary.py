import os
import datetime
import pandas as pd
from typing import List, Dict, Any
import openai

# Load your OpenAI API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- Config ---
DATA_PATH = "./data/trade_log.csv"
default_output_path = f"weekly_summary_{datetime.date.today()}.md"

# --- Helper: Load and Filter Trades ---
def load_trades(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["entry_datetime"] = pd.to_datetime(df["trade_date"] + " " + df["entry_time"])
    df["r_multiple"] = df["profit_points"] / df["risk_level"]
    return df

def filter_last_week(df: pd.DataFrame) -> pd.DataFrame:
    one_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    return df[df["entry_datetime"] >= one_week_ago]

# --- Aggregation Logic ---
def compute_weekly_stats(df: pd.DataFrame) -> Dict[str, Any]:
    total_trades = len(df)
    win_rate = (df["r_multiple"] > 0).mean()
    avg_r = df["r_multiple"].mean()
    total_r = df["r_multiple"].sum()

    top_setups = df["entry_type"].value_counts().nlargest(3).index.tolist()
    common_emotions = df["llm_feedback_summary"].value_counts().nlargest(3).index.tolist()

    return {
        "total_trades": total_trades,
        "win_rate": win_rate,
        "avg_r": avg_r,
        "total_r": total_r,
        "top_setups": top_setups,
        "common_emotions": common_emotions,
    }

# --- Prompt Generator ---
def generate_prompt(stats: Dict[str, Any], sample_notes: List[str], start_date: str, end_date: str) -> str:
    return f"""
Weekly Trading Summary – Week of {start_date} to {end_date}

Stats:
- Total trades: {stats['total_trades']}
- Win rate: {stats['win_rate']:.2%}
- Avg R-multiple: {stats['avg_r']:.2f}
- Total R gain/loss: {stats['total_r']:.2f}
- Most used setups: {', '.join(stats['top_setups'])}
- Common emotions: {', '.join(stats['common_emotions'])}

Sample Trade Notes:
{chr(10).join(sample_notes)}

Based on this data, give a 3–5 paragraph coaching-style summary including:
- Observations on patterns and behaviors
- Emotional tendencies
- Concrete goals for improvement next week
- Reinforcement of good habits
"""

# --- GPT Call ---
def get_gpt_summary(prompt: str, model="gpt-3.5-turbo") -> str:
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content
        if content is None:
            raise ValueError("No content received from OpenAI API")
        return content
    except Exception as e:
        return f"Error generating summary: {str(e)}"

# --- Report Formatter ---
def format_to_markdown(stats: Dict[str, Any], gpt_summary: str, start_date: str) -> str:
    return f"""
# Weekly Trading Summary – Week of {start_date}

## 📊 Stats
- **Total Trades:** {stats['total_trades']}
- **Win Rate:** {stats['win_rate']:.2%}
- **Average R-Multiple:** {stats['avg_r']:.2f}
- **Total R Gain/Loss:** {stats['total_r']:.2f}
- **Top Setups:** {', '.join(stats['top_setups'])}
- **Common Emotions:** {', '.join(stats['common_emotions'])}

---

## 🧠 GPT Coaching Summary

{gpt_summary}

---

*Generated automatically by NeuroSpect.*
"""

# --- Save File ---
def save_markdown_report(content: str, output_path: str = default_output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

# --- Main Pipeline ---
def run_weekly_summary():
    df = load_trades(DATA_PATH)
    df = filter_last_week(df)
    if df.empty:
        print("No trades found in the last 7 days.")
        return

    stats = compute_weekly_stats(df)
    sample_notes = df["notes"].dropna().sample(min(3, len(df))).tolist()

    start_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    end_date = datetime.datetime.now().strftime("%Y-%m-%d")

    prompt = generate_prompt(stats, sample_notes, start_date, end_date)
    gpt_summary = get_gpt_summary(prompt)

    markdown = format_to_markdown(stats, gpt_summary, start_date)
    save_markdown_report(markdown)
    print(f"Weekly summary saved to {default_output_path}")

if __name__ == "__main__":
    run_weekly_summary()