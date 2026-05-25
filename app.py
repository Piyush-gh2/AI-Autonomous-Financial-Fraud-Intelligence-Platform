import streamlit as st

from src.agents import run_fraud_ai
from src.rag import load_knowledge, build_index, retrieve

st.title("💳 AI Autonomous Financial Fraud Intelligence Platform")

query = st.text_input("Ask Financial Intelligence Insight")

if st.button("Analyze Transactions"):

    df, prediction, risk, explanation = run_fraud_ai()

    st.subheader("📊 Financial Transaction Dataset")
    st.dataframe(df)

    st.subheader("📈 Fraud Forecast")
    st.write(f"Predicted Fraud Exposure Score: {prediction:.2f}")

    st.subheader("⚠️ Fraud Detection")
    st.write(risk)

    st.subheader("🧠 Explainable AI Insight")
    st.write(explanation)

    st.bar_chart(df["amount"])

    # RAG
    docs = load_knowledge()
    index = build_index(docs)

    if query:

        insights = retrieve(query, docs, index)

        st.subheader("🔎 Financial Intelligence Insights")

        for i in insights:
            st.write(i)