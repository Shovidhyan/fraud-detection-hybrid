from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.fraud_detector import detect_fraud
from agents.risk_explainer import explain_risk
from agents.decision_agent import make_decision

from agents.block_agent import block_transaction
from agents.review_agent import review_transaction
from agents.allow_agent import allow_transaction


# STATE
class FraudState(TypedDict):
    transaction: str
    fraud_result: dict
    ai_analysis: str
    decision: str
    final_action: str


# AGENT 1 — FRAUD DETECTOR
def fraud_detection_node(state):

    result = detect_fraud(state["transaction"])

    return {
        "fraud_result": result
    }


# AGENT 2 — RISK ANALYZER
def risk_analysis_node(state):

    analysis = explain_risk(state["fraud_result"])

    return {
        "ai_analysis": analysis
    }


# AGENT 3 — DECISION AGENT
def decision_node(state):

    decision = make_decision(state["fraud_result"])

    return {
        "decision": decision
    }


# AGENT 4 — BLOCK AGENT
def block_node(state):

    return block_transaction(state)


# AGENT 5 — REVIEW AGENT
def review_node(state):

    return review_transaction(state)


# AGENT 6 — ALLOW AGENT
def allow_node(state):

    return allow_transaction(state)


# CONDITIONAL ROUTING
def route_decision(state):

    decision = state["decision"]

    if decision == "BLOCK TRANSACTION":
        return "block_agent"

    elif decision == "FLAG FOR MANUAL REVIEW":
        return "review_agent"

    else:
        return "allow_agent"


# BUILD GRAPH
builder = StateGraph(FraudState)


# ADD NODES
builder.add_node("fraud_detector", fraud_detection_node)
builder.add_node("risk_analyzer", risk_analysis_node)
builder.add_node("decision_agent", decision_node)

builder.add_node("block_agent", block_node)
builder.add_node("review_agent", review_node)
builder.add_node("allow_agent", allow_node)


# ENTRY POINT
builder.set_entry_point("fraud_detector")


# NORMAL FLOW
builder.add_edge("fraud_detector", "risk_analyzer")
builder.add_edge("risk_analyzer", "decision_agent")


# CONDITIONAL FLOW
builder.add_conditional_edges(
    "decision_agent",
    route_decision
)


# FINAL EDGES
builder.add_edge("block_agent", END)
builder.add_edge("review_agent", END)
builder.add_edge("allow_agent", END)


# COMPILE GRAPH
graph = builder.compile()


# TEST RUN
if __name__ == "__main__":

    response = graph.invoke({
        "transaction": """
        Multiple failed login attempts detected.
        Unknown IP address.
        Large international money transfer initiated.
        New device login detected.
        """
    })

    print("\nFINAL AI CYBERSECURITY REPORT\n")

    print("Fraud Detection Result:\n")
    print(response["fraud_result"])

    print("\nAI Analysis:\n")
    print(response["ai_analysis"])

    print("\nAUTONOMOUS DECISION:\n")
    print(response["decision"])

    print("\nFINAL SECURITY ACTION:\n")
    print(response["final_action"])