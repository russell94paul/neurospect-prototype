import streamlit as st
from backend.storage import save_trade

def render_submit_button(trade_data, storage_mode):
    st.markdown("## ✅ Submit Trade")

    if st.button("Submit Trade"):
        # Basic validation
        required_fields = ["trade_date", "direction", "entry_type"]
        missing = [field for field in required_fields if not trade_data.get(field)]

        if missing:
            st.error(f"Please fill in all required fields: {', '.join(missing)}")
            return False
        
        # Save the trade using selected mode
        try:
            save_trade(trade_data, mode=storage_mode.lower())
            st.success("✅ Trade logged successfully!")
            return True
        except Exception as e:
            st.error(f"⚠️ Failed to save trade: {str(e)}")
            return False