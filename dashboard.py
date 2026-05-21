import streamlit as st

from graph_workflow import graph


# PAGE SETTINGS
st.set_page_config(
    page_title="AI Cyber Defense System",
    layout="wide"
)


# TITLE
st.title("🛡 AI Cyber Defense System")

st.write("Multi-Agent Fraud Detection using LangGraph")


# USER INPUT
transaction = st.text_area(
    "Enter Transaction Details",
    height=200,
    placeholder="""
Example:
Large money transfer detected.
Unknown login location.
Multiple failed login attempts.
New device access.
"""
)


# BUTTON
if st.button("Analyze Transaction"):

    if transaction.strip() == "":
        st.warning("Please enter transaction details.")
    else:

        response = graph.invoke({
            "transaction": transaction
        })

        # FRAUD RESULT
        st.subheader("Fraud Detection Result")
        st.json(response["fraud_result"])

        # AI ANALYSIS
        st.subheader("AI Security Analysis")
        st.write(response["ai_analysis"])

        # DECISION
        st.subheader("Autonomous Decision")
        st.success(response["decision"])

        # FINAL ACTION
        st.subheader("Final Security Action")
        st.warning(response["final_action"])