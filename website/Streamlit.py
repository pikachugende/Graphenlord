import streamlit as st
import numpy as np
import random

def generate_response():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    return response
    
st.set_page_config(page_title="Graphenlord v1.0", layout="wide")


st.markdown("""

    <style>
    .title {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        color: #3580C5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .matrix-input {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 1rem;
        background-color: #f8f9fa;
        transition: all 0.3s ease;
    }
    .matrix-input:focus-within {
        border-color: #4A90E2;
        box-shadow: 0 0 0 2px rgba(74,144,226,0.2);
    }
    .result-box {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 1.5rem;
        margin-top: 1rem;
        border: 1px solid #e0e0e0;
        color: #333333 !important;
    }
    .result-box pre {
        color: #333333 !important;
        font-family: 'Courier New', monospace !important;
        white-space: pre !important;
        margin: 0;
    }
    .stButton>button {
        background-color: #4A90E2 !important;
        color: white !important;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #357ABD !important;
    }
    </style>
    """, unsafe_allow_html=True)
colu1, colu2, colu3 = st.columns([1, 2, 1])
with colu1:
    st.image("website/Drache.png", width=200)
def multiply_matrices(matrix1_str, matrix2_str):
    try:
        mat1 = np.array([[float(num) for num in row.split()]
                         for row in matrix1_str.strip().split("\n") if row.strip()])
        mat2 = np.array([[float(num) for num in row.split()]
                         for row in matrix2_str.strip().split("\n") if row.strip()])

        result = np.dot(mat1, mat2)
        matrix_str = "Graphenlord sagt:\n"
        for row in result:
            matrix_str += ' '.join(f"{num:8.2f}" for num in row) + "\n"
        return matrix_str.strip()
    except Exception as e:
        return f"❌ Fehler: {str(e)}"


with colu2:
    st.markdown('<div class="title">Graphenlord v1.0</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Matrix A")
    matrix1 = st.text_area(
        "Matrix 1 Input",
        height=200,
        placeholder="Eine Zahl pro Zeile, getrennt durch Leerzeichen\nBeispiel:\n1 2 3\n4 5 6",
        key="m1",
        label_visibility="collapsed"
    )

with col2:
    st.markdown("### Matrix B")
    matrix2 = st.text_area(
        "Matrix 2 Input",
        height=200,
        placeholder="Eine Zahl pro Zeile, getrennt durch Leerzeichen\nBeispiel:\n7 8\n9 10\n11 12",
        key="m2",
        label_visibility="collapsed"
    )

st.write("")  
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Berechne Matrixprodukt", use_container_width=True):
        with st.spinner("Berechnung läuft..."):
            result = multiply_matrices(matrix1, matrix2)

            if "❌" in result:
                st.error(result)
            else:
                st.markdown("### Ergebnis")
                st.markdown(f"<div class='result-box'><pre>{result}</pre></div>",
                            unsafe_allow_html=True)
                



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Sprechen Sie mit einem Experten"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("Graphenlord[Experte]"):
        response_placeholder = st.empty()
        response = ""
        # Assume generate_response() returns an iterable stream of text chunks
        for chunk in generate_response():
            response += chunk
            response_placeholder.markdown(response)
    
    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
