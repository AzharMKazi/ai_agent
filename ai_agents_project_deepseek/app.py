import streamlit as st
from graph_backend import create_graph

st.title("🔍 AI Research Agent")

query = st.text_input("Enter your query:")

if st.button("Run Search & Analyze"):
    if not query:
        st.warning("Please enter a query.")
    else:
        st.info("Processing...")
        graph = create_graph()
        result = graph.invoke({"query": query})
        st.success("✅ Optimized Response:")
        st.markdown(result["final_response"])
