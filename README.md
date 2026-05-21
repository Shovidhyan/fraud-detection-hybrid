# AI Cyber Defense System

## Overview

AI Cyber Defense System is a multi-agent cybersecurity project built using:

- LangGraph
- LangChain
- Streamlit
- Transformers
- OpenRouter LLMs

The system simulates an autonomous AI-powered fraud detection and cybersecurity response workflow.

It analyzes suspicious transactions, explains potential risks using AI, makes autonomous security decisions, and dynamically routes actions through multiple AI agents.

---

# Features

- Multi-Agent AI Architecture
- Fraud Detection using Transformer Models
- AI Risk Analysis using LLMs
- Autonomous Decision Making
- Conditional Routing with LangGraph
- Streamlit Dashboard
- Real-Time Security Analysis
- Modular Agent Design

---

# AI Agents

## 1. Fraud Detection Agent

Detects suspicious transaction patterns using NLP classification.

## 2. Risk Analysis Agent

Uses LLM reasoning to explain why a transaction may be fraudulent.

## 3. Decision Agent

Makes autonomous cybersecurity decisions based on fraud score.

## 4. Block Agent

Blocks high-risk transactions.

## 5. Review Agent

Flags suspicious transactions for manual review.

## 6. Allow Agent

Approves low-risk transactions.

---

# Workflow Architecture

```text
Transaction Input
        ↓
Fraud Detection Agent
        ↓
AI Risk Analyzer
        ↓
Decision Agent
        ↓
Conditional Routing
   ┌────────┼────────┐
   ↓        ↓        ↓
Block    Review    Allow
Agent    Agent     Agent
        ↓
Final Security Action
```

---

# Technologies Used

- Python
- LangGraph
- LangChain
- Streamlit
- HuggingFace Transformers
- OpenRouter API
- BART Large MNLI
- VS Code

---

# Project Structure

```text
fraud-detection-hybrid/
│
├── agents/
│   ├── fraud_detector.py
│   ├── risk_explainer.py
│   ├── decision_agent.py
│   ├── block_agent.py
│   ├── review_agent.py
│   └── allow_agent.py
│
├── app/
│   └── llm.py
│
├── model/
│   └── model_loader.py
│
├── utils/
│   └── preprocess.py
│
├── dashboard.py
├── graph_workflow.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Shovidhyan/fraud-detection-hybrid.git
```

## Move into Project

```bash
cd fraud-detection-hybrid
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment (Windows)

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Streamlit Dashboard

```bash
streamlit run dashboard.py
```

---

# Example Input

```text
Multiple failed OTP attempts detected.
Unknown IP address used.
Large international transfer initiated.
New device login detected.
```

---

# Example Output

- Fraud Detection Result
- AI Security Analysis
- Autonomous Decision
- Final Security Action

---
