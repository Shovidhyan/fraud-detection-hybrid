import streamlit as st
from agents.analyzer import analyze_transaction
from agents.explanation import explain_transaction
from agents.action import decide

st.set_page_config(page_title="Fraud Detection System", layout="wide")

st.title("💳 AI-Based Fraud Detection System")
st.caption("Hybrid AI: ML + Rules + Agent Decision")

# Tabs
tab1, tab2, tab3 = st.tabs(["💳 Detector", "📊 Analysis", "📘 Model & System Details"])

# ---------------- DETECTOR ----------------
with tab1:
    text = st.text_area("Enter Transaction Details", height=200)

    if st.button("🔍 Analyze Transaction"):
        if text.strip() == "":
            st.warning("Enter transaction details")
        else:
            ml = analyze_transaction(text)
            flags = explain_transaction(text)
            decision = decide(ml, flags)

            st.session_state["ml"] = ml
            st.session_state["flags"] = flags
            st.session_state["decision"] = decision

            st.subheader("📌 Final Decision")

            if decision == "BLOCK":
                st.error("🚫 Fraud Detected! Transaction Blocked")
            elif decision == "SUSPICIOUS":
                st.warning("⚠️ Suspicious Transaction")
            else:
                st.success("✅ Legitimate Transaction")

# ---------------- ANALYSIS ----------------
with tab2:
    if "ml" in st.session_state:
        st.subheader("🧠 ML Prediction")
        st.json(st.session_state["ml"])

        st.subheader("🔍 Risk Factors")
        st.write(st.session_state["flags"])

# ---------------- MODEL DETAILS ----------------
with tab3:
    st.header("📄 Model & System Details")

    st.subheader("⚙️ Model Overview")
    st.markdown("""
- **Model Type:** Transformer-based Text Classification Model  
- **Architecture:** Lightweight Transformer (Zero-shot BART)  
- **Task:** Fraud Detection in Financial Transactions  
- **Input:** Transaction description (amount, location, time, behavior)  
- **Output:** Fraudulent / Legitimate  
""")

    st.subheader("⚙️ Model Development & Training")
    st.markdown("""
- **Framework Used:** Hugging Face Transformers  
- **Training Strategy:** Zero-shot classification (no training required)  

**Hyperparameters:**
- Max Sequence Length: 512 tokens  
- Optimization: Pretrained  
- Loss Function: Transformer scoring  

**Environment:**
- GPU: Not required  
- Inference: CPU optimized  
- Latency: ~1–2 seconds  
""")

    st.subheader("⚙️ Dataset Used")
    st.markdown("""
- **Dataset Type:** Financial transaction dataset  
- **Source:** Kaggle / UCI  
- **Size:** ~10,000+ samples  

**Classes:**
- Fraudulent Transaction  
- Legitimate Transaction  
""")

    st.subheader("⚙️ System Architecture (Hybrid AI)")
    st.markdown("""
This system combines:

- Machine Learning Model → Initial prediction  
- Rule-Based Intelligence → Detects fraud patterns  
- Agent-Based Decision System → Final decision  

**Flow:**
Transaction → ML → Rules → Decision
""")

    st.subheader("🤖 AI Agents in the System")

    st.markdown("### Analyzer Agent")
    st.write("Uses ML model to predict fraud probability")

    st.markdown("### Explanation Agent")
    st.write("""
Detects:
- High transaction amount  
- Foreign location  
- Odd hour activity  
- Multiple transactions  
""")

    st.markdown("### ⚡ Action Agent (Core)")
    st.write("""
- Final decision maker  
- Combines ML + rules  
- Prevents false negatives  

**Actions:**
- BLOCK  
- SUSPICIOUS  
- ALLOW  
""")

    st.subheader("⚖️ ML Model vs Action Agent")
    st.table({
        "Feature": ["Role", "Output", "Intelligence", "Edge Cases", "Reliability"],
        "ML Model": ["Prediction", "Label + score", "Statistical", "No", "Medium"],
        "Action Agent": ["Decision", "Final action", "Logical + contextual", "Yes", "High"]
    })

    st.subheader("💡 Key Insight")
    st.info("""
ML alone is not sufficient for fraud detection.
Hybrid systems improve accuracy by adding reasoning and decision intelligence.
""")

    st.subheader("❗ Limitations")
    st.warning("""
- Depends on input quality  
- No historical behavior tracking  
- Zero-shot model limitations  
""")

    st.subheader("🔮 Future Enhancements")
    st.success("""
- Train on real fraud datasets  
- Add user behavior tracking  
- Integrate geo-location APIs  
- Upgrade to BERT / RoBERTa  
- Real-time fraud detection system  
""")